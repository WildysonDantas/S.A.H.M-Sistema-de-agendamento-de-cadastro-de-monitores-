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
        assert "credenciais" in browser.page_source

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

    def testeCadastroEmailContendoApenasEspacos(self):
        browser = self.browser
        print("Teste de Cadastro Completo com email contendo apenas espacos")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("José")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("                     ")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022989")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("jose123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("jose123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroEmailContendoApenasNumeros(self):
        browser = self.browser
        print("Teste de Cadastro Completo com email contendo apenas números")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("José")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("12345678910")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022989")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("jose123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("jose123")
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

    def testeCadastroComNomeContendoApenasEspacos(self):
        browser = self.browser
        print("Teste de Cadastro Completo com o nome contendo apenas espaços")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("                       ")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("jose@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022998")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("jose123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("jose123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroComMatriculaJaCadastrada(self):
        browser = self.browser
        print("Teste de Cadastro Completo com uma matrícula já cadastrada")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("José")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("jose@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("20159022990")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("jose123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("jose123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroComMatriculaContendoApenasLetras(self):
        browser = self.browser
        print("Teste de Cadastro Completo com a matrícula contendo apenas letras")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys(" José de Sousa ")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("jose@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("apenasletrasl")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("jose123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("jose123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

    def testeCadastroComMatriculaContendoApenasEspacos(self):
        browser = self.browser
        print("Teste de Cadastro Completo com a matrícula contendo apenas espaços")
        browser.get('http://127.0.0.1:8000/cadastro/')
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys(" José de Sousa ")
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("jose@hotmail.com")
        elem = browser.find_element_by_id("id_matricula")
        elem.send_keys("           ")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("jose123")
        elem = browser.find_element_by_id("id_conf_senha")
        elem.send_keys("jose123")
        elem.send_keys(Keys.RETURN)
        assert "Cadastre" in browser.page_source

# FIM DOS TESTES REFERENTES A PAGINA DE CADASTRO

# TESTES REFERENTES A PAGINA DE LOGINS

    def test_Login(self):
        browser = self.browser
        print("Teste de Requisicao")
        email= ["widl@gmail.com", "paulo@gmail.com","renesiojoa@hotmail.com"]
        senha = ["opaopa", "paulo123","renesio123"]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(email)):
            #assert "Google" in browser.title
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "Conta" in browser.page_source
            link = browser.find_element_by_link_text('Sair')
            link.click()

    def testeContaInexistente(self):
        browser = self.browser
        print("Teste de conta inexistente")
        email= ["nome@gmail.com"]
        senha = ["senha123"]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(email)):
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "inexistente" in browser.page_source

    def testeContaComSenhaErrada(self):
        browser = self.browser
        print("Teste de conta com senha inválida")
        email= ["paulo@gmail.com"]
        senha = ["senha123"]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(email)):
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "inválida" in browser.page_source

    def testeSenhaEmBranco(self):
        browser = self.browser
        print("Teste de Senha em branco")
        email= ["widl@gmail.com"]
        senha = [""]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(email)):
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "S.A.H.M" in browser.title

    def testeComEmailContendoApenasEspacos(self):
        browser = self.browser
        print("Teste com email contendo apenas espaços")
        email= ["                 "]
        senha = ["andre12"]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(email)):
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "S.A.H.M" in browser.title

    def testeComSenhalContendoApenasEspacos(self):
        browser = self.browser
        print("Teste com senha contendo apenas espaços")
        email= ["widl@gmail.com"]
        senha = ["                   "]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(email)):
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "S.A.H.M" in browser.title

    def testeEmailEmBranco(self):
        browser = self.browser
        print("Teste de Email em branco")
        email= [""]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        for x in range(len(senha)):
            elem = browser.find_element_by_id("id_login")
            elem.send_keys(email[x])
            elem = browser.find_element_by_id("id_senha")
            elem.send_keys(senha[x])
            elem.send_keys(Keys.RETURN)
            assert "S.A.H.M" in browser.title

    def testeEmailSenhaEmBranco(self):
        browser = self.browser
        print("Teste de Email e Senha em branco")
        email= [""]
        senha = [""]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email[0])
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha[0])
        elem.send_keys(Keys.RETURN)
        assert "S.A.H.M" in browser.title

    # FIM DOS TESTES REFERENTES A PAGINA DE LOGINS

    # TESTES REFERENTES A PÁGINA DE CONFIGURAÇÕES DO MONITOR

    def testeEmailVazioNaAlteracaoDeEmail(self):
        browser = self.browser
        print("Teste de alteração de email com campo email vazio")
        email = ["widl@gmail.com"]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text("Configurações de Monitor")
        link.click()
        link = browser.find_element_by_link_text("Alterar Email")
        link.click()
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("opaopa")
        elem.send_keys(Keys.RETURN)
        assert "antigo" in browser.page_source

    def testeAlteracaoEmailContendoApenasEspacos(self):
        browser = self.browser
        print("Teste de alteração de email com campo email contendo apenas espaços")
        email = ["widl@gmail.com"]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text("Configurações de Monitor")
        link.click()
        link = browser.find_element_by_link_text("Alterar Email")
        link.click()
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("                            ")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("opaopa")
        elem.send_keys(Keys.RETURN)
        assert "antigo" in browser.page_source

    def testeAlteracaoEmailContendoNumeros(self):
        browser = self.browser
        print("Teste de alteração de email com campo email contendo numeros")
        email = ["widl@gmail.com"]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text("Configurações de Monitor")
        link.click()
        link = browser.find_element_by_link_text("Alterar Email")
        link.click()
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("123456789")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("opaopa")
        elem.send_keys(Keys.RETURN)
        assert "antigo" in browser.page_source

    def testeAlteracaoEmailSemArroba(self):
        browser = self.browser
        print("Teste de alteração de email com campo email sem a @")
        email = ["widl@gmail.com"]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text("Configurações de Monitor")
        link.click()
        link = browser.find_element_by_link_text("Alterar Email")
        link.click()
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("wildysongmail.com")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("opaopa")
        elem.send_keys(Keys.RETURN)
        assert "antigo" in browser.page_source

    """def testeAlteracaoEmailComSenhaInvalida(self):
        browser = self.browser
        print("Teste de alteração de email com a senha inválida")
        email = ["widl@gmail.com"]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text("Configurações de Monitor")
        link.click()
        link = browser.find_element_by_link_text("Alterar Email")
        link.click()
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("wildyson@gmail.com")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("opaopa123")
        elem.send_keys(Keys.RETURN)
        assert "antigo" in browser.page_source

    def testeAlteracaoEmailSemPontoCom(self):
        browser = self.browser
        print("Teste de alteração de email com campo email sem o .com")
        email = ["widl@gmail.com"]
        senha = ["opaopa"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text("Configurações de Monitor")
        link.click()
        link = browser.find_element_by_link_text("Alterar Email")
        link.click()
        elem = browser.find_element_by_id("id_email")
        elem.send_keys("wildyson@gmail")
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys("opaopa")
        elem.send_keys(Keys.RETURN)
        assert "antigo" in browser.page_source"""

    def testeExclusaoDoMonitor(self):
        browser = self.browser
        print("Teste de exclusão de conta de monitor")
        email = ["tacio@hotmail.com"]
        senha = ["tecioo123"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text('Configurações de Monitor')
        link.click()
        link = browser.find_element_by_link_text('Excluir Conta')
        link.click()
        alert = browser.switch_to_alert()
        alert.accept()
        assert "credenciais" in browser.page_source

    # TESTES REFERENTES A PÁGINA DE CONFIGURAÇÕES DO MONITOR

    # TESTES REFERENTES A PAGINA DE ATUALIZAÇÃO DE DADOS CADASTRAIS
    """
    def testeAtualizacaoDeDadosCadastrais(self):
        browser = self.browser
        print("Teste Completo de atualização dos dados cadastrais")
        email = ["renesiojoa@hotmail.com"]
        senha = ["renesio123"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text('Atualizar Informações Cadastrais')
        link.click()
        elem = browser.find_element_by_id("id_nome")
        elem.send_keys("Renesio Joaquim Oliveira")
        elem = browser.find_element_by_id("id_fone")
        elem.send_keys("8999999999")
        elem = browser.find_element_by_id("id_nascimento")
        elem.send_keys("01/09/1996")
        elem = browser.find_element_by_id("select_curso")
        elem.send_keys('CSHNB - SISTEMAS DE INFORMAÇÃO')
        elem.send_keys(Keys.ENTER)
        elem = browser.find_element_by_id("id_materia")
        elem.send_keys("Estruturas de Dados")
        elem.send_keys(Keys.RETURN)
        assert "alterados" in browser.page_source"""

    # FIM DOS TESTES REFERENTES A PAGINA DE ATUALIZAÇÃO DE DADOS CADASTRAIS

    # TESTES REFERENTES A PÁGINA DE CADASTRO DE MONITORIAS

    def testeCadastroMonitoriaSemInformarMateria(self):
        browser = self.browser
        print("Teste de cadastro de monitoria sem informar a matéria")
        email = ["paulo@gmail.com"]
        senha = ["paulo123"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text('Cadastrar Monitoria')
        link.click()
        assert "prosseguir" in browser.page_source

    def testeCadastroDeMonitoria(self):
        browser = self.browser
        print("Teste completo de cadastro de monitoria")
        email = ["andrelukas91@hotmail.com"]
        senha = ["andre12"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text('Cadastrar Monitoria')
        link.click()
        elem = browser.find_element_by_id("id_sala")
        elem.send_keys("809")
        elem = browser.find_element_by_id("id_dia")
        elem.send_keys("20/09/2018")
        elem = browser.find_element_by_id("id_hora_inicio")
        elem.send_keys("08:00")
        elem = browser.find_element_by_id("id_hora_termino")
        elem.send_keys("10:00")
        elem.send_keys(Keys.RETURN)
        assert "cadastrada" in browser.page_source

    """def testeCadastroDeMonitoriaComCamposVazios(self):
        browser = self.browser
        print("Teste de cadastro de monitoria com campos vazios")
        email = ["andrelukas91@hotmail.com"]
        senha = ["andre12"]
        browser.get('http://127.0.0.1:8000/login/')
        elem = browser.find_element_by_id("id_login")
        elem.send_keys(email)
        elem = browser.find_element_by_id("id_senha")
        elem.send_keys(senha)
        elem.send_keys(Keys.RETURN)
        link = browser.find_element_by_link_text('Cadastrar Monitoria')
        link.click()
        elem = browser.find_element_by_id("id_sala")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_dia")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_hora_inicio")
        elem.send_keys("")
        elem = browser.find_element_by_id("id_hora_termino")
        elem.send_keys("")
        elem.send_keys(Keys.RETURN)
        assert "cadastrada" in browser.page_source"""

    # FIM DOS TESTES REFERENTES A PÁGINA DE CADASTRO DE MONITORIAS