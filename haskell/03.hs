elementAt :: [a] -> Int -> a
elementAt (x:_) 1 = x
elementAt [] _ = error "Index out of bounds"
elementAt (_:xs) n = elementAt xs (n - 1)
