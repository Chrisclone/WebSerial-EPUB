from ebooklib import epub
from HTMLPreper import preper, pages
import os
import time

class writer:
    def __init__(self, urlTable, author, pgCnt, locationF, title):
        self.title = title
        self.author = author
        self.prep = preper(urlTable, pgCnt)
        self.directory = os.path.join(locationF, title + ".epub")
        self.file = open(self.directory, "w")
        self.pager()
    def pager(self):
        try:
            self.book = epub.EpubBook()
            self.book.set_identifier(str(time.time()))
            self.book.set_title(self.title)
            self.book.set_language("en")
            self.book.add_author(self.author)
            self.spine = ["nav"]

            style = "html { font-family: Helvetica, Arial; line-height: 1.6;}"

            css = epub.EpubItem(uid="style_nav",
                                    file_name="style/nav.css",
                                    media_type="text/css",
                                    content=style)
            self.book.add_item(css)

            chapter_count = 1
            for item in self.prep.urls:
                page = pages(item)

                chapter = epub.EpubHtml(title=page.title(), lang="en", file_name=f"Chapter {chapter_count}.xhtml")
                chapter.content = page.mainText()

                self.book.add_item(chapter)
                self.spine.append(chapter)

                chapter_count += 1
        except:
            self.book.spine = self.spine
            epub.write_epub(self.directory, self.book, {})
        finally:
            self.book.spine = self.spine
            epub.write_epub(self.directory, self.book, {})