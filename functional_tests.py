from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Maria entra na página principal
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        # adicionar primeiro item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Estudar testes funcionais')
      
        # Quando ela aperta enter, a página atualiza, e mostra a lista
        # "1: Estudar testes funcionais" como um item da lista TODO
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Estudar testes funcionais')
        
        # Ainda existe uma caixa de texto convidando para adicionar outro item
        # Ela digita: "Estudar testes de unidade"
        inputbox = self.browser.find_element_by_id('id_new_item')  
        inputbox.send_keys('Estudar testes de unidade')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página atualiza novamente, e agora mostra ambos os itens na sua lista
        self.check_for_row_in_list_table('1: Estudar testes funcionais')
        self.check_for_row_in_list_table('2: Estudar testes de unidade')

        # aguardar tabela
        for i in range(10):
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                break
            except Exception:
                time.sleep(0.5)

        self.assertIn('1: Estudar testes funcionais', [row.text for row in rows])

        # adicionar segundo item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Estudar testes de unidade')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Estudar testes funcionais', [row.text for row in rows])
        self.assertIn('2: Estudar testes de unidade', [row.text for row in rows])


if __name__ == '__main__':
    unittest.main()
