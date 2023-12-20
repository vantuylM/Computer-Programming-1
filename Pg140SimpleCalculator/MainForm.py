﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(410, 10)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(76, 53)
		self._button1.TabIndex = 0
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(492, 10)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(76, 53)
		self._button2.TabIndex = 1
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(574, 10)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(76, 53)
		self._button3.TabIndex = 2
		self._button3.Text = "x"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.Maroon
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(410, 69)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(76, 53)
		self._button4.TabIndex = 3
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Maroon
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(492, 66)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(76, 53)
		self._button5.TabIndex = 4
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.Maroon
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(574, 69)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(76, 53)
		self._button6.TabIndex = 5
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.Maroon
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(492, 125)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(76, 53)
		self._button7.TabIndex = 6
		self._button7.Text = "Mod"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.Maroon
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(454, 184)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(158, 53)
		self._button8.TabIndex = 7
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.Maroon
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(454, 243)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(158, 59)
		self._button9.TabIndex = 8
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Red
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(196, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(194, 31)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Red
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(196, 184)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(194, 31)
		self._textBox2.TabIndex = 10
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(196, 81)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(194, 83)
		self._label1.TabIndex = 11
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(63, 28)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(127, 51)
		self._label2.TabIndex = 12
		self._label2.Text = "Num 1"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(45, 81)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(145, 83)
		self._label3.TabIndex = 13
		self._label3.Text = "Operation"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(63, 184)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(127, 61)
		self._label4.TabIndex = 14
		self._label4.Text = "Num 2"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(63, 256)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(113, 53)
		self._label5.TabIndex = 15
		self._label5.Text = "Result"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(196, 243)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(194, 66)
		self._label6.TabIndex = 16
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.ClientSize = System.Drawing.Size(683, 394)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg140SimpleCalculator"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label1.Text = "+"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer = float(num1) + float(num2)
		self._label6.Text = str(answer)

	def Button2Click(self, sender, e):
		self._label1.Text = "-"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer = float(num1) - float(num2)
		self._label6.Text = str(answer)


	def Button3Click(self, sender, e):
		self._label1.Text = "x"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer = float(num1) * float(num2)
		self._label6.Text = str(answer)


	def Button4Click(self, sender, e):
		self._label1.Text = "^"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer = float(num1) ** float(num2)
		self._label6.Text = str(answer)


	def Button5Click(self, sender, e):
		self._label1.Text = "/"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer = float(num1) / float(num2)
		self._label6.Text = str(answer)


	def Button6Click(self, sender, e):
		self._label1.Text = "//"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer = float(num1) // float(num2)
		self._label6.Text = str(answer)


	def Button7Click(self, sender, e):
		self._label1.Text = "MOD"
		num1 = self._textBox1.Text
		num2 = self._textBox2.Text
		answer1 = float(num1) // float(num2)
		answer2 = float(answer1) * float(num2)
		answer3 = float(num1) - float(answer2)
		Final = answer3
		self._label6.Text = str(Final)


	def Button8Click(self, sender, e):
		self._label1.Text = ""
		self._label6.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button9Click(self, sender, e):
		Application.Exit()