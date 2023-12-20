require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Location = System::Drawing::Point.new(282, 34)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(148, 37)
		@label1.TabIndex = 0
		# 
		# label2
		# 
		@label2.Location = System::Drawing::Point.new(282, 71)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(148, 31)
		@label2.TabIndex = 1
		# 
		# label3
		# 
		@label3.Location = System::Drawing::Point.new(282, 102)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(148, 27)
		@label3.TabIndex = 2
		# 
		# label4
		# 
		@label4.Location = System::Drawing::Point.new(282, 129)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(148, 27)
		@label4.TabIndex = 3
		@label4.Click { |sender, e| self.Label4Click(sender, e) }
		# 
		# label5
		# 
		@label5.Location = System::Drawing::Point.new(282, 156)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(148, 33)
		@label5.TabIndex = 4
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlText
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.HotTrack
		@button1.Location = System::Drawing::Point.new(178, 308)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(130, 130)
		@button1.TabIndex = 6
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlText
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.HotTrack
		@button2.Location = System::Drawing::Point.new(383, 308)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(142, 130)
		@button2.TabIndex = 7
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.HotTrack
		self.ClientSize = System::Drawing::Size.new(727, 566)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.ResumeLayout(false)
	end

	def Label4Click(sender, e)
		
	end

	def Button1Click(sender, e)
		@label1.Text = "(608)-752-7521"
		@label2.Text = "(608)-752-9908"
		@label3.Text = "(608)-554-3712"
		@label4.Text = "(608)-756-4343"
		@label5.Text = "(608)-754-0623"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
	end
end

