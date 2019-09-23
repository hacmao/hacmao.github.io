from gmpy2 import gcd, invert, iroot, is_prime 
from Crypto.Util.number import long_to_bytes 

p1 = 282595361018796512312481928903796535047168039821441204226899357708165480989181288601210607191471483534037953052604722708819774231230476577951670676743338887609132820418468389978419501153422449272224388422022777
q1 = 142270506848638924547091203976235495577725242858694711068289574174127601000137457280276860615471044907560710121669055364010408768146949985099404319539891688093875478389341632242096859500255283810703767020918479
k = 877 
p2 = 291668652611471250039066078554824884845341136873092210122454888337748213391694969640183343019452438800975699247613989121123985462360872265327833435184781051854777074884190706087067889456284908187292126902073849
q2 = 90298557884682577669238320760096423994217812898822512514104930945042122418007925771281125855142645396913218673571816112036657123492733042972301983242487835472292994595416656844378721884370309120262139835889657
k = 1041 
p3 = 267307309343866797026967908679365544381223264502857628608660439661084648014195234872217075156454448820508389018205344581075300847474799458610853350116251989700007053821013120164193801622760845268409925117073227
p4 = 188689169745401648234984799686937623590015544678958930140026860499157441295507274434268349194461155162481283679350641089523071656015001291946438485044113564467435184782104140072331748380561726605546500856968771

f = open("output.txt", "r") 
data = f.read().split("\n") 
for i in range(4) : 
    data[i] = map(int, data[i].split(" ")[1:])  
e = 1667 

r = gcd(data[1][0], data[0][0])  
d2 = invert(e, (p1 - 1)*(q1- 1)*(r-1))  
print data[1][0] % q1  
d1 = invert(e, (p2 - 1)*(q2 - 1)*(r - 1)) 

print data[2][0] % (p3 ** 2)
q3 = data[2][0] / (p3**2) 
d3 = invert(e, (p3 - 1)*p3*(q3-1)) 
q4 = data[3][0] / p4 
assert data[3][0] == p4 * q4 
d4 = invert(e, (p4-1)*(q4-1)) 
c = 594744523070645240942929359037746826510854567332177011620057998249212031582656570895820012394249671104987340986625186067934908726882826886403853350036347685535238091672944302281583099599474583019751882763474741100766908948169830205008225271404703602995718048181715640523980687208077859421140848814778358928590611556775259065145896624024470165717487152605409627124554333901173541260152787825789663724638794217683229247154941119470880060888700805864373121475407572771283720944279236600821215173142912640154867341243164010769049585665362567363683571268650798207317025536004271505222437026243088918839778445295683434396247524954340356
c = pow(c, d4, data[3][0]) 
c = pow(c, d3, data[2][0]) 
c = pow(c, d2, data[1][0]) 
c = pow(c, d1, data[0][0])
print long_to_bytes(c)