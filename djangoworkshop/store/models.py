from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True) # uniqe=ห้ามซ้ำกัน
    slug=models.SlugField(max_length=255,unique=True) # slug ใช้ Generate Url และผูกข้อมูลติดกับ Url 

    def __str__(self):
        return self.name  # แปลง object เป็น String

    class Meta :
        ordering=('name',)
        verbose_name='หมวดหมู่สินค้า' # ตั้งชื่อหัวข้อข้างในเมนู
        verbose_name_plural='ข้อมูลประเภทสินค้า' # ตั้งชื่อเมนูหลังบ้าน


class Product(models.Model):
    name=models.CharField(max_length=255,unique=True) #uniqe=ห้ามซ้ำกัน
    slug=models.SlugField(max_length=255,unique=True) #slug ใช้ Generate Url และผูกข้อมูลติดกับ Url 
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2) #decimal places=ทศนิยม 2 ตำแหน่ง
    category=models.ForeignKey(Category,on_delete=models.CASCADE) # คีย์เชื่อมไปยัง ตาราง Category,models.CASCADE=ในกรณีที่ลบแม่ลูกจะหายด้วย
    image=models.ImageField(upload_to="product",blank=True) # blank=true คือ สามารถยังไม่ต้องใส่ภาพได้
    stock=models.IntegerField()
    available=models.BooleanField(default=True) # สถานะ True=โชว์สินค้า, False=ไม่โชว์สินค้า
    created=models.DateTimeField(auto_now_add=True) # วันเวลาที่สร้าง,auto now add=เอาวันเวลา ณ ปัจจุบัน
    updated=models.DateTimeField(auto_now=True) # วันเวลาที่อัพเดท, auto now=วันเวลา ณ ปัจจุบันที่มีการบันทึกข้อมูล
    
    def __str__(self):
        return self.name  # แปลง object เป็น String

    class Meta :
        ordering=('name',)
        verbose_name='สินค้า' # ตั้งชื่อหัวข้อข้างในเมนู
        verbose_name_plural='ข้อมูลสินค้า' # ตั้งชื่อเมนูหลังบ้าน