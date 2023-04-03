import names
import random
from ecommerce.models import Product,ProductType
for i in range(150):
    name = names.get_full_name()
    price = round(random.randint(1000,10000))
    product = Product(
    name = name,
    sku = name,
    type = ProductType.objects.all()[random.randint(2,5)],
    price = price,
    discounted_price = price/2,
    slug = name.replace(" ", "-")
    )
    product.save()