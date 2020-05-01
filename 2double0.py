# coding: UTF-8
import sys
l1l11ljx713 = sys.version_info [0] == 2
l11ll1jx713 = 2048
l1jx713 = 7
def l1l11jx713 (lljx713):
    global l1l1lljx713
    l1l1ljx713 = ord (lljx713 [-1])
    l1lll1jx713 = lljx713 [:-1]
    l1l1jx713 = l1l1ljx713 % len (l1lll1jx713)
    l1ll1jx713 = l1lll1jx713 [:l1l1jx713] + l1lll1jx713 [l1l1jx713:]
    if l1l11ljx713:
        l11llljx713 = unicode () .join ([unichr (ord (l11ljx713) - l11ll1jx713 - (l1lllljx713 + l1l1ljx713) % l1jx713) for l1lllljx713, l11ljx713 in enumerate (l1ll1jx713)])
    else:
        l11llljx713 = str () .join ([chr (ord (l11ljx713) - l11ll1jx713 - (l1lllljx713 + l1l1ljx713) % l1jx713) for l1lllljx713, l11ljx713 in enumerate (l1ll1jx713)])
    return eval (l11llljx713)
import socket
import select
import time
import sys
print l1l11jx713 (u"ࠦࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࠀ")
print l1l11jx713 (u"ࠧࠦࠠࠡࠢࠣࠤࠥࠦࠠࡠࠢࡢࠤࠥࠦࠠࠡࡡࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡥ࡟ࡠࡡࡢࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡠࠢࠣࠤࠥࠦࠠࠡࡡࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࠁ")
print l1l11jx713 (u"ࠨࠠࠡࠢࠣࠤࠥࠦࠠࡽࠢࡿࠤࢁࠦࠠࠡࠪࡢ࠭ࠥࠦࠠࠡࠢࠣࠤࠥ࠵ࠠࡠࡡࡢࡣࢁࠦࠠࠡࠢࠣࠤࠥࠦࠠࠩࡡࠬࠤࠥࠦࠠࠡࡾࠣࢀࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࠂ")
print l1l11jx713 (u"ࠢࠡࠢࠣࠤࠥࠦࠠࠡࡾࠣࢀࠥࢂ࡟ࡠࠢࠣࡣࠥࡥࠠࡠࡡࠣࠤࠥࢂࠠࠩࡡࡢࡣࠥࠦࠠࡠࡡࡢࠤࡤࠦ࡟ࡠࠢࡢࠤࡤࠦ࡟ࡠࠢࡿࠤࢁࡥࠠࡠࡡࡢࠤࡤࠦ࡟ࡠࠢࠣࠤࠧࠃ")
print l1l11jx713 (u"ࠣࠢࠣࠤࠥࡥࠠࠡࠢࡿࠤࢁࠦࠧࡠࠢ࡟ࢀࠥࢂࠠࠨࡡࠣࡠࠥࠦࠠ࡝ࡡࡢࡣࠥࡢࠠ࠰ࠢࡢࡣࢁࠦࠧࡠࡡࡿࠤࢁࠦࠧࡠࠢ࡟ࢀࠥࡥ࡟࠰ࠢࡢࠤࡡࠦࠧࡠࡡࡿࠤࠥࠨࠄ")
print l1l11jx713 (u"ࠤࠣࠤࠥࢂࠠࡽࡡࡢࢀࠥࢂࠠࡽࠢࡿࠤࢁࠦࡼࠡࡾࠣࢀࠥࢂࠠࠡࡡࡢࡣࡤ࠯ࠠࡽࠢࠫࡣࡤࢂࠠࡽࠢࠣࢀࠥࢂࠠࡽࡡࠬࠤࢁࠦࡼࡽࠢࠣࡣࡤ࠵ࠠࡽࠢࠣࠤࠥࠦࠢࠅ")
print l1l11jx713 (u"ࠥࠤࠥࠦࠠ࡝ࡡࡢࡣࡤ࠵ࡼࡠࡾࠣࢀࡤࢂ࡟ࡽࡡࡿࠤࢁࡥࡼࠡࡾࡢࡣࡤࡥ࡟࠰ࠢ࡟ࡣࡤࡥࡼࡠࡾࠣࠤࢁࡥࡼࠡ࠰ࡢࡣ࠴ࠦ࡜ࡠࡡ࡟ࡣࡤࡥࡼࡠࡾࠣࠤࠥࠦࠠࠣࠆ")
print l1l11jx713 (u"ࠦࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡽࠢࡿࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࠇ")
print l1l11jx713 (u"ࠧࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡾࡢࢀࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࠈ")
print l1l11jx713 (u"ࠨࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࠉ")
print l1l11jx713 (u"ࠢࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡎࡖࡗࡩ࡫ࡷࡩࡱ࡯ࡳࡵࠢࡅࡽࡵࡧࡳࡴࠢ࠮ࠤࡈࡵ࡮ࡴࡱ࡯ࡩ࠲ࡕࡵࡵࡲࡸࡸࠥࡍࡲࡢࡤࡥࡩࡷࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࠊ")
print l1l11jx713 (u"ࠣࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࠋ")
l1llll1jx713 = raw_input(l1l11jx713 (u"ࠤࡌࡔ࠿ࠦࠢࠌ"))
l111ljx713 = input(l1l11jx713 (u"ࠥࡔࡴࡸࡴࡢ࠼ࠣࠦࠍ"))
buffer_size = 4096
l1111jx713 = 0.0001
l11l11jx713 = (l1llll1jx713, l111ljx713)
data = l1l11jx713 (u"ࠦ࠳࠴࠯࠯࠰࠲࠲࠳࠵ࠢࠎ")
print l1l11jx713 (u"ࠧࡉ࡯࡯ࡧࡻࣧࡴࠦࡳࡰࡥ࡮ࡩࡹࡹࠠࡢࡤࡨࡶࡹࡧࠠࡦ࡯ࠣࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠶࠷࠸ࠥࠏ")
class l1llljx713:
    def __init__(self):
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self, host, port):
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception, e:
            print e
            return False
class l1111ljx713:
    l111jx713 = []
    l1ll11jx713 = {}
    def __init__(self, host, port):
        self.l1llllljx713 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.l1llllljx713.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.l1llllljx713.bind((host, port))
        self.l1llllljx713.listen(200)
    def l1lljx713(self):
        self.l111jx713.append(self.l1llllljx713)
        while 1:
            time.sleep(l1111jx713)
            l11111jx713 = select.select
            l1l111jx713, l11lljx713, l11l1jx713 = l11111jx713(self.l111jx713, [], [])
            for self.s in l1l111jx713:
                if self.s == self.l1llllljx713:
                    self.l111lljx713()
                    break
                self.data = self.s.recv(buffer_size)
                if len(self.data) == 0:
                    self.l11l1ljx713()
                    break
                else:
                    self.l111l1jx713()
    def l111lljx713(self):
        forward = l1llljx713().start(l11l11jx713[0], l11l11jx713[1])
        l11jx713, l1l1l1jx713 = self.l1llllljx713.accept()
        if forward:
            print l1l1l1jx713, l1l11jx713 (u"ࠨࡃࡰࡰࡱࡩࡨࡺࡥࡥࡀࠣࡘࡗ࡛ࡅࠣࠐ")
            self.l111jx713.append(l11jx713)
            self.l111jx713.append(forward)
            self.l1ll11jx713[l11jx713] = forward
            self.l1ll11jx713[forward] = l11jx713
        else:
            print l1l11jx713 (u"ࠢࡏࣥࡲࠤ࡫ࡵࡩࠡࡲࡲࡷࡸ࡯ࡶࡦ࡮ࠣࡩࡸࡺࡡࡣࡧ࡯ࡩࡨ࡫ࡲࠡࡥࡲࡲࡪࡾࣣࡰࠢࡦࡳࡲࠦ࡯ࠡࡵࡨࡶࡻ࡯ࡤࡰࡴࠣࡶࡪࡳ࡯ࡵࡱࠤ࠲ࠧࠑ"),
            print l1l11jx713 (u"ࠣࡇࡵࡶࡴࠦࡤࡦࠢࡦࡳࡳ࡫ࡸࣤࡱࠣࡲࡴࠦ࡬ࡢࡦࡲࠤࡩࡵࠠࡤ࡮࡬ࡩࡳࡺ࠮ࠣࠒ"), l1l1l1jx713
            l11jx713.close()
    def l11l1ljx713(self):
        print self.s.getpeername(), l1l11jx713 (u"ࠤࡩࡳ࡮ࠦࡤࡦࡵࡦࡳࡳ࡫ࡣࡵࡣࡧࡳ࠳ࠨࠓ")
        self.l111jx713.remove(self.s)
        self.l111jx713.remove(self.l1ll11jx713[self.s])
        l1ll1ljx713 = self.l1ll11jx713[self.s]
        self.l1ll11jx713[l1ll1ljx713].close()
        self.l1ll11jx713[self.s].close()
        del self.l1ll11jx713[l1ll1ljx713]
        del self.l1ll11jx713[self.s]
    def l111l1jx713(self):
        data = self.data
        print data
        self.l1ll11jx713[self.s].send(data)
if __name__ == l1l11jx713 (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬࠔ"):
    l1llllljx713 = l1111ljx713(l1l11jx713 (u"ࠫࡱࡵࡣࡢ࡮࡫ࡳࡸࡺࠧࠕ"), 666)
    try:
        l1llllljx713.l1lljx713()
    except KeyboardInterrupt:
        print l1l11jx713 (u"ࠧࡉࡴࡳ࡮࠮ࡇࠥࡶࡡࡳࡣࠣࡩࡳࡩࡥࡳࡴࡤࡶࠥࡧࠠࡤࡱࡱࡩࡽࣩ࡯ࠡࡵࡲࡧࡰ࡫ࡴࡴ࠰ࠥࠖ")
        sys.exit(1)