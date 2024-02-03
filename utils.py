
def validate_image_extensions(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.svg', '.png', '.jpg', '.jpeg', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 3.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


def validate_ir_national_code(national_id):
    fake_codes = [
        "1234567890",
        "0000000000",
        "1111111111",
        "2222222222",
        "3333333333",
        "4444444444",
        "5555555555",
        "6666666666",
        "7777777777",
        "8888888888",
        "9999999999",
    ]
    if len(national_id) < 10:
        return False

    if national_id in fake_codes:
        return False
    national_id = "0" * (len(national_id) - 10) + national_id
    national_id = list(map(int, national_id[::-1]))
    temp = 0
    for index, digit in enumerate(national_id[1:]):
        temp += digit * (index + 2)
    r = divmod(temp, 11)[1]
    if r < 2 and r == national_id[0]:
        return True
    elif r >= 2 and (11 - r) == national_id[0]:
        return True
    return False


def validate_ir_phones(value):
    val = str(value)
    iran_operator_list = ['0939', '0938', '0937', '0936', '0935', '0933', '0930', '0905',
                          '0903', '0902', '0901', '0900',
                          '0990', '0991', '0992', '0993', '0994', '0919', '0910',
                          '0911', '0912', '0913', '0914', '0915', '0916',
                          '0917', '0918', '0932',
                          '0922', '0921', '0920', '0931', '0934']

    pre_numbers = val[0:4]
    if pre_numbers not in iran_operator_list:
        raise ValidationError("پیش شماره همراه معتبر نیست.")
