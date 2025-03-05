import pdbp
from seleniumbase import BaseCase

url = 'https://www.nytimes.com/games/wordle/index.html'

class Wordle(BaseCase): 
    row = 1 # row number (which guess we're on) <= 6

    def test_wordle(self): 
        self.headless = False
        self.open(url)
        self.click_if_visible('button.purr-blocker-card__button', timeout=2)
        self.click_if_visible('button:contains("Play")', timeout=2)
        self.click_if_visible('svg[data-testid="icon-close"]', timeout=2)
        self.remove_elements('div.place-ad')

        self.sleep(2)
        self.send_keys('body', 'ADIEU\n', timeout=2)
        self.row += 1
        self.sleep(2)
        self.send_keys('body', 'BLOCK\n', timeout=2)
        self.row += 1
        self.sleep(2)
        self.send_keys('body', 'SYNTH\n', timeout=2)
        self.row += 1
        try: 
            row_n = self.find_elements('[aria-label="Row 1"] > div') # the n'th row
            for i in row_n:
                div = i.find_element(By.CSS_SELECTOR, 'div[style="animation-delay: 100ms"]')
                print(div) 

        except Exception as e:
            print(f'Error: {e}')
        breakpoint()



