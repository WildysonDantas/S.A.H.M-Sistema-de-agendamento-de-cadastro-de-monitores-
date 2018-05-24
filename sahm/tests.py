from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome(executable_path=r"/home/andre/PDSI/S.A.H.M-Sistema-de-agendamento-de-cadastro-de-monitores-/sahm/chromedriver")
class MonitorTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"/home/andre/PDSI/S.A.H.M-Sistema-de-agendamento-de-cadastro-de-monitores-/sahm/chromedriver")

    def tearDown(self):
        self.browser.quit()

    #TESTES REFERENTES A PAGINA DE CADASTRO

    def testeCadastroCompleto(self):
        browser = self.browser
        print("Teste de Cadastro Completo")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("Tecio Joaquim")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("tacio@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022993")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("tecioo123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("tecioo123")
        elem.send_keys(Keys.RETURN)
        assert "Conta" in browser.page_source

    def testeCadastroNomeVazio(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Nome Vazio")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("renesiojoa@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("201520451400")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("renesio123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("renesio123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroMatriculaVazio(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Matricula Vazia")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("Renesio Joaquim")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("renesiojoa@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("renesio123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("renesio123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroEmailVazio(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Email Vazio")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("Renesio")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("201520451400")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("renesio123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("renesio123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroSenhaVazio(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Senha Vazio")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("Renesio")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("renesiojoa@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("201520451400")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("renesio123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroConfSenhaVazio(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Confirmacao de Senha Vazio")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("renesiojoa@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("201520451400")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("renesio123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroEmBranco(self):
        browser = self.browser
        print("Teste de Cadastro em Branco")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroSenhaNaoConfere(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Senhas que nao Conferem")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("Renesio")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("renesiojoa@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("201520451400")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("renesio123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("renesio1234")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroEmailSemArroba(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Email sem o '@'")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("André")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("andrehotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022997")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("andre123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("andre123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroEmailSemPontoCom(self):
        browser = self.browser
        print("Teste de Cadastro Completo com Email sem o '.com'")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("André")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("andre@hotmail")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022997")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("andre123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("andre123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroComSenhaContendoMenosDe6Caracteres(self):
        browser = self.browser
        print("Teste de Cadastro Completo com senha contendo menos de 6 caracteres")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("André")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("andre@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022997")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("andre")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("andre")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroComMatriculaContendoMenosDe11Caracteres(self):
        browser = self.browser
        print("Teste de Cadastro Completo com a matricula contendo menos de 11 caracteres")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("André")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("andre@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("2015902299")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("andre123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("andre123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

