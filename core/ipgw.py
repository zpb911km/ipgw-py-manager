# main ipgw progress
from requests import Session
from .requestresult import UnionAuth, SuccessPage, Device
from bs4 import BeautifulSoup
from .errors_modals import *


# 描述一个ipgw统一身份认证的全过程。
class IPGW:
    # 初始化，获得一个ipgw的统一身份认证界面
    def __init__(self):
        self.sess = Session()
        self.sess.headers.update({'User-Agent': ua})
        self.union_auth_page: UnionAuth = None

        self.last_trial_times = -1
        self.success_page: SuccessPage = None

    def login(self, username, password):
        union_auth_page_soup = BeautifulSoup(self.sess.get(target).text, 'lxml')
        self.union_auth_page = UnionAuth(union_auth_page_soup)
        try:
            self.success_page = self.union_auth_page.login(username, password, self.sess)
        except UnionAuthError as e:
            if type(e) is UnionAuthError:
                self.last_trial_times = e.last_trial_times
                return LoginResult.UsernameOrPasswordError
            elif type(e) is AttemptReachLimitError:
                self.last_trial_times = -1
                return LoginResult.AttemptReachLimit
        # 没有异常
        return LoginResult.LoginSuccessful

    def logout(self, sid: str):
        Device.logout_sid(sid, self.sess)

    def get_ipgw_status(self) -> PageStatus:
        sp = self.success_page
        if sp.status == PageStatus.Normal:
            # 如果一切正常，则继续获取流量等信息
            sp.get_detailed_traffic_and_online_seconds(self.sess)
        return sp.status

    def get_current_device(self) -> Device:
        # 找到当前设备
        current_device = next((x for x in self.success_page.device_list if x.is_current), None)
        if not current_device:
            raise NoCurrentDeviceError
        else:
            return current_device

    def logout_online_others(self):
        Device.logout_sid(self.success_page.online_other_uid, self.sess)

    def advanced_logout(self, logout_all_devices=False, only_keep_self=False, only_logout_self=False):
        logout_self = logout_all_devices or only_logout_self
        logout_others = logout_all_devices or only_keep_self
        for device in self.success_page.device_list:
            if device.is_current and logout_self:
                device.logout(self.sess)
            if not device.is_current and logout_others:
                device.logout(self.sess)