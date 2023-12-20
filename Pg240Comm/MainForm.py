import System.Drawing
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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(12, 439)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(128, 64)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Red
		self._button2.Location = System.Drawing.Point(146, 439)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(128, 64)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(280, 439)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(128, 64)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(75, 75)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(114, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Sales For The Month:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(75, 118)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(128, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Advanced Pay Awarded:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(89, 259)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Commission Rate:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(89, 295)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Commission:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(89, 345)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Net Pay:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(209, 78)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(209, 121)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 9
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(209, 259)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "label6"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(209, 295)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(209, 345)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 12
		self._label8.Text = "label8"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Cyan
		self.ClientSize = System.Drawing.Size(408, 506)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		rate = int(self._textBox.Text)
		if rate < 10000:
			self._label6.Text = "5%"
			comm = 0.05
			Thing = int(self._textBox2.Text)
			
		elif rate > 10000 and rate <= 14999:
			self._label6.Text = "10%"
			comm = 0.1
		elif rate > 14999 and rate < 17999:
			self._label6.Text = "12%"
			comm = 0.12
		elif rate > 17999 and rate < 21999:
			self._label6.Text = "14%"
			comm = 0.14
		elif rate > 22000:
			self._label6.Text = "16%"
			comm = 0.16

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()