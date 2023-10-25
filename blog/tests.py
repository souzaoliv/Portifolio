from django.test import TestCase, Client


# Create your tests here.
class TestPaginaTemplates(TestCase):

    def test_index(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_sobre(self):
        response = self.client.get('/blog/sobre/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/sobre.html')

    def test_detail_post(self):
        response = self.client.get('/blog/detail_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail_post.html')

class TestMetodosHttpIndex(TestCase):
    def test_get(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
    def test_post(self):
        response = self.client.post('/blog/')
        self.assertEqual(response.status_code, 405)
    def test_put(self):
        response = self.client.put('/blog/')
        self.assertEqual(response.status_code, 405)
    def test_delete(self):
        response = self.client.delete('/blog/')
        self.assertEqual(response.status_code, 405)
class TestMetodosHttpSobre(TestCase):
    def test_get(self):
        response = self.client.get('/blog/sobre/')
        self.assertEqual(response.status_code, 200)
    def test_post(self):
        response = self.client.post('/blog/sobre/')
        self.assertEqual(response.status_code, 405)
    def test_put(self):
        response = self.client.put('/blog/sobre/')
        self.assertEqual(response.status_code, 405)
    def test_delete(self):
        response = self.client.delete('/blog/sobre/')
        self.assertEqual(response.status_code, 405)

class TestMetodosHttpDetailpost(TestCase):
    def test_post(self):
        response = self.client.get('/blog/detail_post/')
        self.assertEqual(response.status_code, 200)
    def test_get(self):
        response = self.client.post('/blog/detail_post/')
        self.assertEqual(response.status_code, 405)
    def test_put(self):
        response = self.client.put('/blog/detail_post/')
        self.assertEqual(response.status_code, 405)
    def test_delete(self):
        response = self.client.delete('/blog/detail_post/')
        self.assertEqual(response.status_code, 405)
