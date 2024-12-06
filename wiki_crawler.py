import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import get_base_url


class Node:
    # TODO: напишите конструктор класса
    pass


class BFS:
    # TODO: напишите конструктор класса

    def push_node(self, node):
        # TODO: напишите логику добавления нового узла
        # TODO: узел нужно добавлять в конец nodes
        # TODO: узел не нужно добавлять, если он уже был посещен
        pass

    def pop_node(self):
        # TODO: напишите логику получения очередного узла
        # TODO: если nodes пустой, то нужно вернуть None
        # TODO: иначе нужно вернуть нулевой элемент (и убрать его из nodes)
        pass


class WikiCrawler(scrapy.Spider):
    name = "wiki"
    start_urls = [
        # random article from russian wikipedia
        "https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
    ]
    link_extractor = LinkExtractor()
    cur = None
    bfs = BFS()

    def __parse_title(self, response):
        """
        Extracts article title.
        Usually article titles looks like "XYZ - Wikipedia", where XYZ - actual topic
        """
        return response.selector.xpath("//title/text()").get()

    def __parse_links(self, response, steps):
        """
        Creates nodes from current page links.
        Links are searched only inside article text.
        All links that redirect NOT to russian wikipedia are skipped.
        """
        nodes = []
        body_selector = response.xpath('//div[@class="mw-content-ltr mw-parser-output"]')
        if not body_selector:
            return nodes
        body_selector = body_selector[0]
        link_extractor = self.link_extractor.link_extractor
        base_url = get_base_url(response)

        for link in link_extractor._extract_links(body_selector, response.url, response.encoding, base_url):
            url = link.url
            if not url.startswith("https://ru.wikipedia.org"):
                continue
            idx = url.rfind('#')
            if idx != -1:
                url = url[:idx]
            nodes.append(Node(title=str(link.text), prev=self.cur, steps=steps, url=url))
        return nodes

    def __build_path(self, node):
        # TODO: напишите логику конструирования строки с путем от начального узла до текущего
        # TODO: строка вида "X -> Y -> Z", где X - начальная статья (название); Y, Z - переходы (текст ссылок)
        pass

    def __show_path(self, node):
        """
        Shows path to Mordor and amount of steps it took to get there.
        """
        print(f'''
                Found Mordor in {node.steps}!
                ------
                Path was:
                {self.__build_path(node)} 
                ''')

    def __find_relevant(self, nodes):
        # TODO: напишите фильтрацию очередных узлов, которые мы будем обходить
        # TODO: можно придумать свой алгоритм фильтрации, можно воспользоваться тем, что описан далее
        # TODO: базовый алгоритм фильтрации:
        # TODO: 1) если один из узлов содержит слово "Мордор" в заголовке, то возвращаем список только с ним
        # TODO: 2) если узел содержит в заголовке что-то из 'Властелин колец', 'Толкин', 'Англи', 'Фэнтэзи', то добавляем его в результирующий список
        # TODO: 3) если в итоге в результирующем списке есть хотя бы один узел, то возвращаем этот список
        # TODO: 4) иначе возвращаем начальный список узлов
        pass

    def parse(self, response, **kwargs):
        # TODO: напишите основную функцию работы со статьей
        # 1. получите заголовок статьи (__parse_title)
        # 2. напечатайте название статьи на экран
        # 3. проинициализируйте cur, если он None (url можно взять через response.url)
        # 4. проверьте, не дошли ли мы до финальной статьи ("Мордор - Википедия")
        # 4.1 если дошли, то покажите полный путь и количество шагов (__show_path)
        # 5. получите ссылки из статьи в виде узлов (__parse_links) и отфильтруйте их (__find_relevant)
        # 6. добавьте получившиеся узлы в список обхода (bfs.push_node)
        # 7. установите новый текущий узел в cur (bfs.pop_node)
        # 8. проверьте, что узлы не закончились (если это так, то в 7 мы получили None)
        # 8.1 если они закончились, то напечатайте, что мы не смогли найти путь и выйдите из метода
        # 9. иначе вызовите функцию заново с помощью yield (yield response.follow(self.cur.url, self.parse))
        pass
