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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Indigo
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 138)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(148, 103)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Indigo
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 283)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(148, 103)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Indigo
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 419)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(148, 103)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Navy
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(147, 122)
		self._label1.TabIndex = 3
		self._label1.Text = "Kilowatt hours:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.BlueViolet
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(166, 55)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(552, 40)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Purple
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(166, 102)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(552, 454)
		self._label2.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateBlue
		self.ClientSize = System.Drawing.Size(730, 565)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		X = float(self._textBox1.Text)
		Money = X * .0475
		Tax = Money * 0.03
		Sur = Money * .10
		TotalBill = Money + Sur + Tax
		LateFee = TotalBill * 0.04
		LateBill = TotalBill + LateFee
		Money = round(Money, 2)
		Tax = round(Tax, 2)
		Sur = round(Sur, 2)
		TotalBill = round(TotalBill, 2)
		LateFee = round(LateFee, 2)
		LateBill = round(LateBill, 2)
		
		self._label2.Text = " C O M P S C I Eletric \t_____________________________________________\t             Kilowatts used                 " + str(self._textBox1.Text) + "\t_____________________________________________\t Base Rate  " + str(self._textBox1.Text) + " @ $ 0.0475  $ " + str(Money) + "\t                 Surcharge                                $ " + str(Sur) + "\t                                        CityTax                                  $ " + str(Tax) + "\t_____________________________________________\t Pay this amount                $" + str(TotalBill) + "\t                                      After May 20th pay                 $ " + str(LateBill)

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()