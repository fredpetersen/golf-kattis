n, _ = gets.split().map(&:to_i)
winner = 0
winner_score = nil

n.times do |i|
  player = i + 1
  score = gets.split.map(&:to_i).sum
  winner = player if winner_score.nil? || score < winner_score
end

p winner