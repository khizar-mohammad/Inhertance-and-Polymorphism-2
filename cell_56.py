#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
  self._name = ""
  self._address = ""
  def __init__(self,name,address):
    self._name = name
    self._address = address
  def GetName(self):
    return self._name
  def GetAddress(self):
    return self._address
  def SetAddress(self,address):
    self._address = address

class Student(Person):
  self.__program = ""
  self.__year = 0
  self.__fee = 0.0
  def __init__(self,program,year,fee,name2,address2):
    Person.__init__(self,name2,address2)
    self.__program = program
    self.__year = year
    self.__fee = fee
  def GetProgram(self):
    return self.__program
  def SetProgram(self,program):
    self.__program = program
  def GetYear(Self):
    return self.__year
  def GetFee(self):
    return self.__fee
  def SetFee(self,fee):
    self.__fee = fee

class Staff(Person):
  self.__school = ""
  self.__pay = 0.0
  def__init__(self,name2,address2,school,pay):
    Person.__init__(self,name2,address2)
    self.__school = school
    self.__pay = pay
  def GetSchool(self):
    return self.__school
  def SetSchool(self,school):
    self.__school = school
  def GetPay(self):
    return self.__pay
  def SetPay(self,pay):
    self.__pay = pay

