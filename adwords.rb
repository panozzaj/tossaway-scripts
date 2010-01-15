# adwords generator

def combine(a, b)
  ret = []
  b.flatten.each do |two|
    a.flatten.each do |one|
      next if one.nil? && two.nil?
      if one.nil?
        ret << two
      elsif two.nil?
        ret << one
      else
        ret << "#{one} #{two}"
      end
    end
  end
  return ret
end

def plur(a)
  [a, "#{a}s"]
end

def ing(s)
  [s, "#{s}ing"]
end


# an example for some product targeting coffee mug sales people
sell = [combine([nil, "how to"], combine([nil, "start"], [ing("sell")]))]
subject_matter = combine(["coffee", "hot beverage"], [plur("mug"), plur("cup"), "glass", "glasses"])
materials = [plur("workshop"), plur("movie"), plur("video"), "video series", "course", "online", "online course", "book", "guide", "ebook", "manual"]

result = combine(sell, subject_matter) + combine(subject_matter, materials)

puts result.flatten
