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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Firebrick
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 433)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(211, 121)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate:"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Firebrick
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(256, 433)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(211, 121)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Firebrick
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(502, 433)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(211, 121)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit:"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(138, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(131, 67)
		self._label1.TabIndex = 3
		self._label1.Text = "Price:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(138, 116)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(131, 67)
		self._label2.TabIndex = 4
		self._label2.Text = "Paid:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Coral
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(275, 43)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(264, 40)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Coral
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(275, 130)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(264, 40)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(167, 240)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(132, 47)
		self._label3.TabIndex = 7
		self._label3.Text = "Quarter:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(167, 287)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(132, 47)
		self._label4.TabIndex = 9
		self._label4.Text = " Dime:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(167, 334)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(132, 47)
		self._label5.TabIndex = 10
		self._label5.Text = "Nickel:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(167, 381)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(132, 47)
		self._label6.TabIndex = 11
		self._label6.Text = "Pennies:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(167, 187)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(130, 53)
		self._label7.TabIndex = 12
		self._label7.Text = "Dollar:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(322, 187)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(190, 53)
		self._label8.TabIndex = 17
		self._label8.Text = " "
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(322, 381)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(192, 47)
		self._label9.TabIndex = 16
		self._label9.Text = " "
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(322, 334)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(192, 47)
		self._label10.TabIndex = 15
		self._label10.Text = " "
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(322, 287)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(192, 47)
		self._label11.TabIndex = 14
		self._label11.Text = " "
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(322, 240)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(192, 47)
		self._label12.TabIndex = 13
		self._label12.Text = " "
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCoral
		self.ClientSize = System.Drawing.Size(725, 566)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""

	def Button1Click(self, sender, e):
		Price = float(self._textBox1.Text)
		Paid = float(self._textBox2.Text)
		Change = Paid - Price
		Dollars = Change // 1
		Quarters = (Change - Dollars) // 0.25
		Dimes = (Change - Dollars - (Quarters / 4)) // 0.10
		Nickels = (Change - Dollars - (Quarters / 4) - (Dimes / 10)) // 0.05
		Pennies = (Change - Dollars - (Quarters / 4) - (Dimes / 10) - (Nickels / 20)) // 0.01
		self._label8.Text = "Dollars: " + str(Dollars)
		self._label12.Text = "Quarters: " + str(Quarters)
		self._label11.Text = "Dimes: " + str(Dimes)
		self._label10.Text = "Nickels: " + str(Nickels)
		self._label9.Text = "Pennies: " + str(Pennies)
		
		