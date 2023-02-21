#! /usr/bin/env ruby

n, _ = gets.split().map(&:to_i)
winner = [nil, nil]
n.times do |i|
  player = i + 1
  score = gets.split.map(&:to_i).sum
  winner = [player, score] if score < winner[1]
end

p winner[0]