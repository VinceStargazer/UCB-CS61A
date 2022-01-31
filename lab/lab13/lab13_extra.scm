; Q4
(define (rle s)
  'YOUR-CODE-HERE
    (define (helper rest last n)
        (if (null? rest)
            (cons-stream (list last n) nil)
            (if (eq? (car rest) last)
                (helper (cdr-stream rest) last (+ n 1))
                (cons-stream (list last n) (helper (cdr-stream rest) (car rest) 1)))))
    (if (null? s)
        nil
        (helper (cdr-stream s) (car s) 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  'YOUR-CODE-HERE
    (define (helper prev rest)
        (if (null? rest)
            (append prev (list n))
            (if (<= n (car rest))
                (append (append prev (list n)) rest)
                (helper (append prev (list (car rest))) (cdr rest)))))
    (helper nil s)
  )

; Q6
(define (deep-map fn s)
  'YOUR-CODE-HERE
    (if (null? s)
        nil
        (if (list? (car s))
            (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
            (cons (fn (car s)) (deep-map fn (cdr s)))))
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  'YOUR-CODE-HERE
    (if (null? s)
        nil
        (cons (car s) (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)

(define (count name s)
  'YOUR-CODE-HERE
    (if (null? s)
        0
        (if (eq? name (car s))
            (+ 1 (count name (cdr s)))
            (count name (cdr s))))
)

(define (tally names)
  'YOUR-CODE-HERE
    (if (null? names)
        nil
        (map (lambda (x) (cons x (count x names))) (unique names)))
)