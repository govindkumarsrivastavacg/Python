t = True
f = False

res_add = t + f
res_sub = t - f
res_mul = t * f
res_div = t / True  
res_fdiv = t // True
res_mod = t % True
res_pow = t ** f

print("Addition (True + False):", res_add, "| Type:", type(res_add))
print("Subtraction (True - False):", res_sub, "| Type:", type(res_sub))
print("Multiplication (True * False):", res_mul, "| Type:", type(res_mul))
print("Division (True / True):", res_div, "| Type:", type(res_div))
print("Floor Division (True // True):", res_fdiv, "| Type:", type(res_fdiv))
print("Modulus (True % True):", res_mod, "| Type:", type(res_mod))
print("Exponentiation (True ** False):", res_pow, "| Type:", type(res_pow))