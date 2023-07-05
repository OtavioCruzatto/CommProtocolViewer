import crc8


class PacoteDeDados:
    __quantidade_de_pacotes: int = 0


    def __init__(self) -> None:
        self.__tamanho_do_pacote: int = 0
        self.__qtd_de_dados: int = 0

        self.__inicilizador_1: int = -1
        self.__inicilizador_2: int = -1
        self.__comando: int = -1
        self.__dados: list[int] = []
        self.__pacote_de_dados: list[int] = []
        self.__crc8: int = -1
        self.__valido: bool = False

        PacoteDeDados.__quantidade_de_pacotes += 1


    def __str__(self) -> str:
        if self.__valido:
            pacote_status = "Valido"
        else:
            pacote_status = "Invalido"

        return (f"Status: {pacote_status}\n"
                f"Byte inicializador 1: {hex(self.__inicilizador_1)}\n"
                f"Byte inicializador 2: {hex(self.__inicilizador_2)}\n"
                f"Qtd de bytes no pacote: {len(self)}\n"
                f"Qtd de bytes de dados: {self.get_quantidade_de_dados()}\n"
                f"Comando: {hex(self.get_comando())}\n"
                f"CRC8 (Polinomio 0x07): {hex(self.__crc8)}\n"
                f"Dados: {[hex(byte) for byte in self.__dados]}\n"
                f"Pacote: {[hex(byte) for byte in self.__pacote_de_dados]}\n")


    def __len__(self) -> int:
        return self.get_tamanho()


    def __del__(self) -> None:
        PacoteDeDados.__quantidade_de_pacotes -= 1


    def montar(self, inicializador_1: int, inicializador_2: int, comando: int, dados: list[int] = []) -> None:
        self.set_inicializador_1(inicializador_1)
        self.set_inicializador_2(inicializador_2)
        self.set_comando(comando)
        self.set_dados(dados)
        self.atualizar()


    def decodificar(self, pacote: list[int]) -> None:
        if (type(pacote) is not list):
            raise TypeError("Variavel 'pacote' deve ser do tipo list.")

        if (len(pacote) > 260):
            raise ValueError("Variavel 'pacote' pode conter no maximo 260 elementos.")

        if (len(pacote) < 5):
            raise ValueError("Variavel 'pacote' deve conter no minimo 5 elementos.")

        if any(not isinstance(byte, int) for byte in pacote):
            raise ValueError("Elementos da variavel 'pacote' devem ser do tipo int.")

        if any((byte < 0) or (byte > 255) for byte in pacote):
            raise ValueError("Elementos da variavel 'pacote' devem ser inteiros entre 0 e 255.")

        if PacoteDeDados.__checar_crc8_polinomio_0x07(pacote) is True:
            self.set_inicializador_1(pacote[0])
            self.set_inicializador_2(pacote[1])
            self.set_comando(pacote[2])
            qtd_de_dados_informado_no_pacote = pacote[3]
            if qtd_de_dados_informado_no_pacote != 0:
                self.set_dados(pacote[4:-1])
            self.__crc8 = pacote[-1]
            self.__tamanho_do_pacote = len(pacote)
            self.__pacote_de_dados = pacote
            if (self.__qtd_de_dados != qtd_de_dados_informado_no_pacote):
                raise ValueError("Quantidade de dados informada incorreta.")
            self.__valido = True
        else:
            raise ValueError("Falha na verificacao do CRC. Obs: CRC8 (polinomio 0x07).")


    def set_inicializador_1(self, inicializador_1: int) -> None:
        if (type(inicializador_1) is not int):
            raise TypeError("Variavel 'inicializador_1' deve ser do tipo int.")

        if (inicializador_1 < 0x00) or (inicializador_1 > 0xff):
            raise ValueError("Variavel 'inicializador_1' deve estar entre 0 (0x00) e 255 (0xff).")

        self.__inicilizador_1 = inicializador_1


    def get_inicializador_1(self) -> int:
        return self.__inicilizador_1


    def set_inicializador_2(self, inicializador_2: int) -> None:
        if (type(inicializador_2) is not int):
            raise TypeError("Variavel 'inicializador_2' deve ser do tipo int.")

        if (inicializador_2 < 0x00) or (inicializador_2 > 0xff):
            raise ValueError("Variavel 'inicializador_2' deve estar entre 0 (0x00) e 255 (0xff).")

        self.__inicilizador_2 = inicializador_2


    def get_inicializador_2(self) -> int:
        return self.__inicilizador_2


    def set_comando(self, comando: int) -> None:
        if (type(comando) is not int):
            raise TypeError("Variavel 'comando' deve ser do tipo int.")

        if (comando < 0x01) or (comando > 0xfe):
            raise ValueError("Variavel 'comando' deve estar entre 1 (0x01) e 254 (0xfe).")

        self.__comando = comando


    def get_comando(self) -> int:
        return self.__comando


    def get_pacote(self) -> list[int]:
        return self.__pacote_de_dados


    def set_dados(self, dados: list[int]) -> None:
        if (type(dados) is not list):
            raise TypeError("Variavel 'dados' deve ser do tipo list.")

        if (len(dados) > 255):
            raise ValueError("Variavel 'dados' pode conter no maximo 255 elementos.")

        if any(not isinstance(dado, int) for dado in dados):
            raise TypeError("Elementos da variavel 'dados' devem ser do tipo int.")

        if any((dado < 0) or (dado > 255) for dado in dados):
            raise ValueError("Elementos da variavel 'dados' devem ser inteiros entre 0 e 255.")

        self.__dados = dados
        self.__qtd_de_dados = len(self.__dados)


    def get_dados(self) -> list[int]:
        return self.__dados


    def atualizar(self) -> None:
        if (self.__inicilizador_1 == -1):
            raise ValueError("Variavel 'inicializador_1' nao definida.")

        if (self.__inicilizador_2 == -1):
            raise ValueError("Variavel 'inicializador_2' nao definida.")

        if (self.__comando == -1):
            raise ValueError("Variavel 'comando' nao definida.")

        self.__valido = False
        self.__pacote_de_dados.clear()
        self.__pacote_de_dados.append(self.__inicilizador_1)
        self.__pacote_de_dados.append(self.__inicilizador_2)
        self.__pacote_de_dados.append(self.__comando)
        self.__pacote_de_dados.append(self.__qtd_de_dados)

        if (self.__qtd_de_dados != 0):
            for dado in self.__dados:
                self.__pacote_de_dados.append(dado)

        self.__calcular_crc8_polinomio_0x07()
        self.__pacote_de_dados.append(self.__crc8)
        self.__tamanho_do_pacote = len(self.__pacote_de_dados)
        self.__valido = True


    def get_tamanho(self) -> int:
        return self.__tamanho_do_pacote


    def get_quantidade_de_dados(self) -> int:
        return self.__qtd_de_dados


    def __calcular_crc8_polinomio_0x07(self):
        crc_8 = crc8.crc8()
        pacote_de_dados_bytes = bytes(self.__pacote_de_dados)
        crc_8.update(pacote_de_dados_bytes)
        crc_8_calculado = int(crc_8.hexdigest(), 16)
        if (crc_8_calculado < 0) or (crc_8_calculado > 255):
            raise ValueError("Erro no calculo do CRC8")
        self.__crc8 = crc_8_calculado


    @staticmethod
    def __checar_crc8_polinomio_0x07(pacote: list[int]) -> bool:
        crc_8 = crc8.crc8()
        pacote_de_dados_bytes = bytes(pacote[0:-1])
        crc_8.update(pacote_de_dados_bytes)
        crc_8_calculado = int(crc_8.hexdigest(), 16)
        crc_8_status = (crc_8_calculado == pacote[-1])
        return crc_8_status


    def esta_valido(self) -> bool:
        return self.__valido


    def get_crc8(self) -> int:
        return self.__crc8


    @staticmethod
    def get_quantidade_de_pacotes() -> int:
        return PacoteDeDados.__quantidade_de_pacotes
