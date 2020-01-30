---
layout : post
title : Fuzzing simple program with angr 
--- 

# Mở đầu   
Chúc các đạo hữu năm mới khoái hoạt. 😁😁😁 
Khai xuân đầu năm mình có học một chút về [```angr```](https://docs.angr.io/). Cái này cũng đọc lâu rồi nhưng xưa thấy khó quá với lười nên lại thôi. Đầu năm tinh thần phấn khởi, lại tìm được mấy bài [writeup](https://blog.efiens.com/tag/ctf/) về angr của team efiens thấy khá hay và dễ hiểu nên mình quyết định tìm hiểu thêm về nó.🥳🥳🥳   
Sau khi đọc xong writeup trên thì mình có tổng kết sơ lại được các bước thực hiện của Angr tại [đây](https://www.notion.so/Basic-Setup-998957b22a5a4c05a077a4851b2e1da0)   


# Simple Program   
Quay trở lại đề tài, sau khi nắm bắt được một số bước cơ bản tiếp cận angr, mình lại tiếp tục cày [tutorial này](https://github.com/jakespringer/angr_ctf/tree/master/solutions). Nó cho ta những challenge dạng ctf đơn giản và nhưng công cụ thực hiện khác nhau giúp ta nắm bắt thêm các cách sử dụng linh hoạt của angr trong từng trường hợp khác nhau.🙂🙂🙂 Cuối cùng, nó có trình bày một bài fuzzing và mình thấy khá là thú vị nên note lại ở đây.   
Chương trình bao gồm 2 hàm cơ bản :   

![](https://raw.githubusercontent.com/hacmao/hacmao.github.io/master/ctf/temp/fuzzAngr1%20(1).PNG)    

![](/ctf/temp/fuzzAngr1 (2).PNG)

