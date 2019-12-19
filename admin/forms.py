# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.fields import FileField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Regexp, Email

from app.models import Admin, Tag, Auth, Role

tags = Tag.query.all()
auth_list = Auth.query.all()
role_list = Role.query.all()

#管理员登陆表单
class LoginForm(FlaskForm):
    account = StringField(
        label='账号',
        validators=[
            DataRequired("请输入账号!")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired("请输入密码!")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            # "required": "required"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在!")

#标签表单
class TagForm(FlaskForm):
    name = StringField(
        label="名称",
        validators=[
            DataRequired("请输入标签！")
        ],
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )
    submit = SubmitField(
        '添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )

#电影便奥丹
class MovieForm(FlaskForm):
    title = StringField(
        label="名称",
        validators=[
            DataRequired("请输入名称")
        ],
        description="名称",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入名称！"
        }
    )
    url = FileField(
        label="文件",
        validators=[
            DataRequired("请上传文件！")
        ],
        description="文件",
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("请输入简介")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    logo = FileField(
        label="摄影",
        validators=[
            DataRequired("请上传摄影！")
        ],
        description="摄影",
    )
    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请选择星级！")
        ],
        coerce=int,
        choices=[(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")],
        description="星级",
        render_kw={
            "class": "form-control",
        }
    )
    tag_id = SelectField(
        label="标签",
        validators=[
            DataRequired("请选择标签！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        description="标签",
        render_kw={
            "class": "form-control",
        }
    )
    area = StringField(
        label="地区",
        validators=[
            DataRequired("请输入地区")
        ],
        description="地区",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区！"
        }
    )
    length = StringField(
        label="大小",
        validators=[
            DataRequired("请输入大小")
        ],
        description="大小",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入大小！"
        }
    )
    release_time = StringField(
        label="上传时间",
        validators=[
            DataRequired("请选择上传时间")
        ],
        description="上传时间",
        render_kw={
            "class": "form-control",
            "placeholder": "请选择上传时间！",
            "id": "input_release_time"
        }
    )
    submit = SubmitField(
        '添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )

#预览表单
class PreviewForm(FlaskForm):
    title = StringField(
        label="预览标题",
        validators=[
            DataRequired("请输入预览标题！")
        ],
        description="预览",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入预览标题！"
        }
    )
    logo = FileField(
        label="预览封面",
        validators=[
            DataRequired("请上传预览封面！")
        ],
        description="预览封面",
    )
    submit = SubmitField(
        '添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )

#修改密码表单
class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label='旧密码',
        validators=[
            DataRequired("请输入旧密码!")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码！",
            # "required": "required"
        }
    )
    new_pwd = PasswordField(
        label='新密码',
        validators=[
            DataRequired("请输入新密码!")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码！",
            # "required": "required"
        }
    )
    submit = SubmitField(
        '修改',
        render_kw={
            "class": "btn btn-primary",
        }
    )

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session["admin"]
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(pwd):
            raise ValidationError("旧密码错误！")

#权限表单
class AuthForm(FlaskForm):
    name = StringField(
        label="权限名称",
        validators=[
            DataRequired("请输入权限名称！")
        ],
        description="权限名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标权限名称！"
        }
    )
    url = StringField(
        label="权限地址",
        validators=[
            DataRequired("请输入权限地址！")
        ],
        description="权限地址",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标权限地址！"
        }
    )
    submit = SubmitField(
        '添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )

#角色表单
class RoleForm(FlaskForm):
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired("请输入角色名称!"),
        ],
        description='角色名称',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入角色名称！"
        }
    )
    auths = SelectMultipleField(
        label='权限列表',
        validators=[
            DataRequired("请选择权限!"),
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in auth_list],
        description='权限列表',
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )

#管理员表单
class AdminForm(FlaskForm):
    name = StringField(
        label='管理员名称',
        validators=[
            DataRequired("请输入管理员名称!")
        ],
        description="管理员名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员名称！",
            # "required": "required"
        }
    )
    pwd = PasswordField(
        label='管理员密码',
        validators=[
            DataRequired("请输入管理员密码!")
        ],
        description="管理员密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员密码！",
            # "required": "required"
        }
    )
    repwd = PasswordField(
        label='管理员重复密码',
        validators=[
            DataRequired("请输入管理员重复密码!"),
            EqualTo('pwd', message="两次密码不一致！")
        ],
        description="管理员重复密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员重复密码！",
            # "required": "required"
        }
    )
    role_id = SelectField(
        label="所属角色",
        coerce=int,
        choices=[(v.id, v.name) for v in role_list],
        render_kw={
            "class": "form-control"
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )

#会员详情表单
class UserdetailForm(FlaskForm):
    name = StringField(
        label="名称",
        validators=[
            DataRequired("请输入标签！")
        ],
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！"
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("请输入手机！"),  # Email("邮箱格式不正确")
            Regexp("1[3458]\\d{9}", message="手机格式不正确")
        ],
        description="手机",
        render_kw={
            "class": "form-control ",
            "placeholder": "请输入手机！"
        }
    )
    face = FileField(
        label="头像",
        validators=[
            DataRequired("请上传头像！")
        ],
        description="头像",
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("请输入简介")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success",
        }
    )
