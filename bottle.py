import pdbp
from seleniumbase import BaseCase

url = 'https://www.nytimes.com/games/wordle/index.html'

class Wordle(BaseCase):

    def test_wordle(self):
        self.headless = False
        self.open(url)
        self.click_if_visible('button.purr-blocker-card__button', timeout=2)
        self.click_if_visible('button:contains("Play")', timeout=2)
        self.click_if_visible('svg[data-testid="icon-close"]', timeout=2)
        self.remove_elements('div.place-ad')

        self.sleep(2)
        self.send_keys('body', 'ADIEU\n', timeout=2)
        sself.sleep(2)
        self.send_keys('body', 'BLOCK\n', timeout=2)
        self.sleep(2)
        self.send_keys('body', 'SYNTH\n', timeout=2)
        breakpoint()
