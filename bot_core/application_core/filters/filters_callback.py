from aiogram.filters.callback_data import CallbackData


class CallbackUser(CallbackData, prefix="id", sep="|"):
    user_id: int


class CallBackYTdata(CallbackUser, prefix="y", sep="|"):
    audio: bool
    itag: int


class CallBackTRdata(CallbackUser, prefix="tr", sep="|"):
    pass


class CallBackSettingsData(CallbackUser, prefix="set", sep="|"):
    button: str