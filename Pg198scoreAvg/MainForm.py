import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(108, 11)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(164, 45)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Three Test Scores"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(58, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Score 1:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(58, 109)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Score 2:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(58, 164)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Score 3:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(58, 222)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Average:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(108, 53)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(164, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(108, 109)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(164, 20)
		self._textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(108, 164)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(164, 20)
		self._textBox3.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Brown
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(19, 289)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 61)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate Average"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Brown
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(171, 259)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 53)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Brown
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(171, 318)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 54)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(108, 222)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(164, 23)
		self._label6.TabIndex = 12
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(58, 239)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(107, 47)
		self._label7.TabIndex = 13
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Brown
		self.ClientSize = System.Drawing.Size(295, 393)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg198scoreAvg"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Score1 = float(self._textBox1.Text)
		Score2 = float(self._textBox2.Text)
		Score3 = float(self._textBox3.Text)
		Average = (Score1 + Score2 + Score3) / 3
		AverageScore = self._label6.Text = str(Average)
		self._label6.Text = str(Average)
		if Average > 95:
			self._label7.Text = "Congratulations! Great Job!"

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()