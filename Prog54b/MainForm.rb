﻿require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox


class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::SystemColors.MenuHighlight
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(321, 7)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(328, 40)
		@textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		@textBox2.BackColor = System::Drawing::SystemColors.MenuHighlight
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(321, 53)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(328, 40)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.BackColor = System::Drawing::SystemColors.MenuHighlight
		@textBox3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(321, 99)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(328, 40)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.BackColor = System::Drawing::SystemColors.MenuHighlight
		@textBox4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(321, 145)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(328, 40)
		@textBox4.TabIndex = 3
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(177, 332)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(472, 57)
		@label1.TabIndex = 5
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(177, 251)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(472, 57)
		@label2.TabIndex = 6
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(165, 13)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(132, 172)
		@label3.TabIndex = 7
		@label3.Text = "Integers"
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(37, 251)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(134, 42)
		@label4.TabIndex = 8
		@label4.Text = "Sum"
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(37, 347)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(134, 42)
		@label5.TabIndex = 9
		@label5.Text = "Average"
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveBorder
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(48, 438)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(202, 116)
		@button1.TabIndex = 10
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveBorder
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(273, 438)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(202, 116)
		@button2.TabIndex = 11
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ActiveBorder
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(491, 437)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(202, 116)
		@button3.TabIndex = 12
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(721, 565)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def MainFormLoad(sender, e)
		
	end

	def MainFormLoad(sender, e)
		
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
	end

	def Button1Click(sender, e)
		Num1 = int(@textBox1.Text)
		Num2 = int(@textBox2.Text)
		Num3 = int(@textBox3.Text)
		Num4 = int(@textBox4.Text)
		Sum = Num1 + Num2 + Num3 + Num4
		Average = Sum/4.0
		@label2.Text = "Sum: " + str(Sum)
		@label1.Text = "Average " + str(Average)
	end
end

