from django.test import TestCase
from .models import Cliente, Cuenta, Transaccion

class ClienteModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Test Usuario",
            email="test@example.com",
            telefono="123456789"
        )

    def test_cliente_creado_correctamente(self):
        self.assertEqual(self.cliente.nombre, "Test Usuario")
        self.assertEqual(self.cliente.email, "test@example.com")
        print("✅ Test 1: Cliente creado correctamente")

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), "Test Usuario")
        print("✅ Test 2: Método __str__ funciona correctamente")

    def test_cliente_email_unico(self):
        clientes = Cliente.objects.filter(email="test@example.com")
        self.assertEqual(clientes.count(), 1)
        print("✅ Test 3: Email único validado correctamente")


class CuentaModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Test Cliente",
            email="cuenta@example.com"
        )
        self.cuenta = Cuenta.objects.create(
            cliente=self.cliente,
            numero_cuenta="001-TEST",
            tipo="ahorro",
            saldo=1000
        )

    def test_cuenta_creada_correctamente(self):
        self.assertEqual(self.cuenta.numero_cuenta, "001-TEST")
        self.assertEqual(self.cuenta.saldo, 1000)
        print("✅ Test 4: Cuenta creada correctamente")

    def test_cuenta_relacionada_con_cliente(self):
        self.assertEqual(self.cuenta.cliente.nombre, "Test Cliente")
        print("✅ Test 5: Relación Cuenta-Cliente funciona correctamente")


class TransaccionModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Test Trans",
            email="trans@example.com"
        )
        self.cuenta = Cuenta.objects.create(
            cliente=self.cliente,
            numero_cuenta="002-TEST",
            tipo="corriente",
            saldo=5000
        )
        self.transaccion = Transaccion.objects.create(
            cuenta=self.cuenta,
            tipo="deposito",
            monto=500,
            descripcion="Prueba de depósito"
        )

    def test_transaccion_creada_correctamente(self):
        self.assertEqual(self.transaccion.tipo, "deposito")
        self.assertEqual(self.transaccion.monto, 500)
        print("✅ Test 6: Transacción creada correctamente")

    def test_transaccion_relacionada_con_cuenta(self):
        self.assertEqual(self.transaccion.cuenta.numero_cuenta, "002-TEST")
        print("✅ Test 7: Relación Transacción-Cuenta funciona correctamente")


class ClienteViewTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Vista Test",
            email="vista@example.com"
        )

    def test_lista_clientes(self):
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, 200)
        print("✅ Test 8: Vista lista clientes responde correctamente")

    def test_crear_cliente(self):
        response = self.client.post('/clientes/nuevo/', {
            'nombre': 'Nuevo Cliente',
            'email': 'nuevo@example.com',
            'telefono': '999999999'
        })
        self.assertEqual(Cliente.objects.count(), 2)
        print("✅ Test 9: Vista crear cliente funciona correctamente")