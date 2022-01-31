; Q1
(define (compose-all funcs)
  (if (null? funcs)
    (lambda (x) x)
    (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))) 
)

; Q2
(define (tail-replicate x n)
  (define (helper res lst)
    (if (= res 0)
      lst
      (helper (- res 1) (cons x lst))))
  (helper n nil)
)