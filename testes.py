
import unittest

from conversoes import (
    rgb_para_hex,
    rgb_para_binario,
    hex_para_rgb,
    binario_para_rgb
)

from validacoes import (
    validar_rgb,
    validar_hex,
    validar_binario
)

class TestesConversoes(unittest.TestCase):

    # TESTE 1: Conversão das cores primárias

    def test_cores_primarias(self):

        self.assertEqual(
            rgb_para_hex(255, 0, 0),
            "#FF0000"
        )

        self.assertEqual(
            rgb_para_hex(0, 255, 0),
            "#00FF00"
        )

        self.assertEqual(
            rgb_para_hex(0, 0, 255),
            "#0000FF"
        )

    # TESTE 2: Limites dos canais RGB

    def test_limites_rgb(self):

        self.assertEqual(
            rgb_para_hex(0, 0, 0),
            "#000000"
        )

        self.assertEqual(
            rgb_para_hex(255, 255, 255),
            "#FFFFFF"
        )

    # TESTE 3: Conversão de HEX para RGB

    def test_hex_para_rgb(self):

        self.assertEqual(
            hex_para_rgb("#FF0000"),
            (255, 0, 0)
        )

        self.assertEqual(
            hex_para_rgb("#00FF00"),
            (0, 255, 0)
        )

        self.assertEqual(
            hex_para_rgb("#0000FF"),
            (0, 0, 255)
        )

    # TESTE 4: Conversão de BIN para RGB

    def test_binario_para_rgb(self):

        self.assertEqual(
            binario_para_rgb(
                "11111111 00000000 00000000"
            ),
            (255, 0, 0)
        )

        self.assertEqual(
            binario_para_rgb(
                "00000000 11111111 00000000"
            ),
            (0, 255, 0)
        )

        self.assertEqual(
            binario_para_rgb(
                "00000000 00000000 11111111"
            ),
            (0, 0, 255)
        )


    # TESTE 5: Validação de valores RGB

    def test_validacao_rgb(self):

        self.assertTrue(validar_rgb(0, 128, 255))

        self.assertFalse(validar_rgb(-1, 128, 255))

        self.assertFalse(validar_rgb(256, 128, 255))


    # TESTE 6: Validação de valores HEX

    def test_validacao_hex(self):

        self.assertTrue(validar_hex("#FF0000"))

        self.assertTrue(validar_hex("00FF00"))

        self.assertFalse(validar_hex("#GG0000"))

        self.assertFalse(validar_hex("#12345"))


    # TESTE 7: Validação de valores BIN

    def test_validacao_binario(self):

        self.assertTrue(
            validar_binario("11111111 00000000 00000000")
        )

        self.assertFalse(
            validar_binario("1111111 00000000 00000000")
        )

        self.assertFalse(
            validar_binario("11111111 00000000 0000000X")
        )


    # TESTE 8: Conversões entre todos os formatos

    def test_conversoes_entre_formatos(self):

        # RGB para BIN
        binario = rgb_para_binario(255, 0, 0)

        self.assertEqual(
            binario,
            "11111111 00000000 00000000"
        )

        # HEX para BIN
        rgb = hex_para_rgb("#00FF00")
        binario = rgb_para_binario(*rgb)

        self.assertEqual(
            binario,
            "00000000 11111111 00000000"
        )

        # BIN para HEX
        rgb = binario_para_rgb(
            "00000000 00000000 11111111"
        )

        hexadecimal = rgb_para_hex(*rgb)

        self.assertEqual(
            hexadecimal,
            "#0000FF"
        )




if __name__ == "__main__":
    unittest.main(verbosity=2)
