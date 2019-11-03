from icrawler.builtin import GoogleImageCrawler
crawler = GoogleImageCrawler(storage={"root_dir":"dogs"})
crawler.crawl(keyword="陵辱 ロリ 二次元", max_num=10)
