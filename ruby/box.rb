#!/usr/bin/ruby -w

class Box
	def initialize(w,h)
		@width, @height = w, h
	end

	def getWidth
		@width
	end
	
	def getHeight
		@height
	end
	
	def setWidth=(value)
		@width = value
	end
	def setHeight=(value)
		@height = value
	end
end

box = Box.new(10, 20)

box.setWidth = 40

x = box.getWidth()
y = box.getHeight()

puts "Width of Box : #{x}"
puts "Height of Box : #{y}"
