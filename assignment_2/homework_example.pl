L <- We sort the the input with decreasing scores of f:
Fp <- TP <- 0
R <- 0
i <- 1
while i <= L do
	if f(i) != fprev then
	push (FP/N, TP/P) onto R
	fprev <- f(i)
	end if

	if L[i] is positive:
	TP <- TP + 1
	else FP <- FP + 1
	i = i + 1
end while
push(FP/N,TP/P)
end