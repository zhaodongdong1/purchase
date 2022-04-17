#历史原值(history_value)=单价(unit_price)  0<原值<999999999
#残值率(residual_value_rate)    0<=残值率<=0.05
#已提折旧月数(depreciation_months)   0<=月数=<预计使用年限
#月折旧额(monthly_depreciation)    0<=月折旧额<=（账面价值(book_value)-历史原值*残值率(history_value)*(residual_value_rate)）
#预计使用年限（月）(use_months)   0<=年限=<864
#计提减值准备额(impairment_provision)   0<=准备额=<（历史原值(history_value)-累计折旧(accumulated_depreciation)-残值(history_value)*(residual_value_rate)）
#账面价值(book_value)  历史原值(history_value)-累计折旧(accumulated_depreciation)-计提减值准备额(impairment_provision)
#账面净值(net_book_value)   历史原值(history_value)-累计折旧(accumulated_depreciation)
#账面原值
history_value = 100
#残值率
residual_value_rate = 0.05
#已提折旧月数
depreciation_months = 12
#预计使用年限（月）
use_months = 72
#计提减值
impairment_provision = 12
#累计折旧
accumulated_depreciation = 66
#月折旧额，单独修改月折旧时传入值，如未修改则不传
monthly_depreciation = ''


#返回单价和账面原值
def history_value_def(history_value):
    unit_price = history_value
    return '单价为%s，账面原值为%s'%(unit_price,history_value)
#校验残值率并且返回月折旧额
def residual_value_rate_def(residual_value_rate):
    monthly_depreciation = history_value*residual_value_rate
    return '月折旧额为%s'%monthly_depreciation

#校验已提折旧月数0<=月数=<预计使用年限use_months
def depreciation_months_def(depreciation_months):
    if depreciation_months <= use_months:
        return '已提折旧月数校验通过'
    else:
        return '已提折旧月数大于预计使用年限，请检查！'


#校验月折旧额是否满足条件0<=月折旧额<=（账面价值(book_value)-历史原值*残值率(history_value)*(residual_value_rate)）
def monthly_depreciation_def(monthly_depreciation=''):
    if monthly_depreciation != '':
        book_value = book_value_def()
        primary_monthly_depreciation = book_value - history_value*residual_value_rate
        if int(monthly_depreciation) >= 0 and int(monthly_depreciation) <= int(primary_monthly_depreciation):
            return '月折旧额满足条件'
        else:
            return '月折旧额不满足条件，请检查！'
    #月折旧额计算公式（历史原值-累计折旧-计提减值准备额）* [（1-残值率）/（预计使用年限月数- 已提折旧月数）* 100%]
    elif monthly_depreciation == '':
        monthly_depreciation = (history_value - accumulated_depreciation-impairment_provision)*(1-residual_value_rate)/(use_months - depreciation_months)
        return '月折旧额为%s'%monthly_depreciation



#校验预计使用年限是否满足状态0<=年限=<864
def use_months_def(use_months):
    if use_months >= 0  and use_months <= 72:
        return '预计使用年限校验通过'
    else:
        return '预计使用年限超72月了，请检查！'

# 校验计提减值准备额是否满足条件impairment_provision，0<=准备额=<（历史原值(history_value)-累计折旧(accumulated_depreciation)-残值(history_value)*(residual_value_rate)）
def impairment_provision_def(impairment_provision):
    aa = history_value - accumulated_depreciation - history_value*residual_value_rate
    if impairment_provision >= 0 and impairment_provision <= aa:
        return '计提减值准备额符合要求'
    else:
        return '计提减值准备额不合符要求，请检查！'

#计算账面价值book_value，历史原值(history_value)-累计折旧(accumulated_depreciation)-计提减值准备额(impairment_provision)
def book_value_def():
    book_value = history_value - accumulated_depreciation - impairment_provision
    return book_value

#计算账面净值，net_book_value，历史原值(history_value)-累计折旧(accumulated_depreciation)
def net_book_value_def():
    net_book_value = history_value - accumulated_depreciation
    return '账面净值为%s'%net_book_value

#判断折旧状态
def judge_depreciation_status():
    if book_value_def() == history_value*residual_value_rate:
        return '折旧状态为已完成折旧'
    else:
        return '折旧状态为提折旧'

a = [history_value_def(history_value),
     residual_value_rate_def(residual_value_rate),
     depreciation_months_def(depreciation_months),
     monthly_depreciation_def(monthly_depreciation),
     use_months_def(use_months),
     impairment_provision_def(impairment_provision),
     {'账面价值为':book_value_def()},
     net_book_value_def(),
     judge_depreciation_status()
     ]
print(a)
