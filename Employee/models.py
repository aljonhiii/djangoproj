# Employee/models.py
from django.db import models

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.dname
    

    class Meta:
        db_table = 'dept'
        
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=10, decimal_places=2)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    
    class Meta:
        db_table = 'emp'