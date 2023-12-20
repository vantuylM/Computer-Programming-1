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
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Yellow
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 471)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(174, 83)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(278, 471)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(174, 83)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Yellow
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(542, 471)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(174, 83)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(100, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(182, 69)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter tickets sold for each type of seat"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(433, 28)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(182, 69)
		self._label2.TabIndex = 4
		self._label2.Text = "Revenue"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(100, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(102, 28)
		self._label3.TabIndex = 5
		self._label3.Text = """Class A:
"""
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(100, 231)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(102, 27)
		self._label4.TabIndex = 6
		self._label4.Text = "Class B:"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(100, 336)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(88, 39)
		self._label5.TabIndex = 7
		self._label5.Text = "Class C:"
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(498, 273)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(179, 65)
		self._label9.TabIndex = 16
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(478, 184)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(168, 77)
		self._label10.TabIndex = 15
		# 
		# label11
		# 
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(478, 100)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(168, 84)
		self._label11.TabIndex = 14
		# 
		# label12
		# 
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(390, 285)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(88, 39)
		self._label12.TabIndex = 13
		self._label12.Text = "Class C:"
		# 
		# label13
		# 
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(390, 205)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(102, 27)
		self._label13.TabIndex = 12
		self._label13.Text = "Class B:"
		# 
		# label14
		# 
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(390, 130)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(102, 28)
		self._label14.TabIndex = 11
		self._label14.Text = """Class A:
"""
		# 
		# label15
		# 
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(353, 338)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(139, 37)
		self._label15.TabIndex = 17
		self._label15.Text = "Total Revenue"
		# 
		# label16
		# 
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(495, 338)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(182, 69)
		self._label16.TabIndex = 18
		self._label16.Click += self.Label16Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(191, 156)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(157, 31)
		self._textBox1.TabIndex = 19
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(191, 231)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(157, 31)
		self._textBox2.TabIndex = 20
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(191, 332)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(157, 31)
		self._textBox3.TabIndex = 21
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(728, 566)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg186Seating"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		# A $15 B $12 C $9
		ClassA = int(self._textBox1.Text)
		ClassB = int(self._textBox2.Text)
		ClassC = int(self._textBox3.Text)
		ClassAFinal = ClassA * 15.00
		ClassBFinal = ClassB * 12.00
		ClassCFinal = ClassC * 9.00
		Revenue = ClassAFinal + ClassBFinal + ClassCFinal
		self._label11.Text = str(ClassAFinal)
		self._label10.Text = str(ClassBFinal)
		self._label9.Text = str(ClassCFinal)
		self._label16.Text = str(Revenue)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label11.Text = ""
		self._label10.Text = ""
		self._label9.Text = ""
		self._label16.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label16Click(self, sender, e):
		pass