# NonLibC_ROP_ATTACK

<p>While learning about ROP and doing ROP CTF problems I created a template for NON LIBC ROP Attacks resulting in reverse shells</p>

<h1>What is an ROP?</h1>
<p>Essentially when you perform a traditional buffer overflow attack you normally cant execute shell code on the stack. ROP
or Return Oriented Programming, manipulates your control of the return pointer to jump around the program file and executes
gadgets of code. You can link all of these gadgets of code together to form a maliciousScript. This link works bc everytime you
leave with a return SP is increased, then when you come back you can return on the new point where SP is. A good video
that explains it is here <a href="https://www.youtube.com/watch?v=8zRoMAkGYQE&list=PLchBW5mYosh_F38onTyuhMTt2WGfY-yr7&index=11"> ROPS EXPLAINED</a>

</p>
