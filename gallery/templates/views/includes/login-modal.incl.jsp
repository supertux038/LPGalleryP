<%@page pageEncoding="UTF-8" %>
<%--<%@include file="reg-modal.peb" %>--%>

<div class="modal fade login-modal" id="sign-in" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle"
     aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="sign-in-modal">Вход</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <form name="login" action="login" method="post">
                <div class="modal-body">

                    <div class="auth-login mb-3">
                        <label for="auth-login">
                            <h5>Логин</h5>
                        </label>
                        <input id="auth-login" class="form-control" type="text" required>
                    </div>
                    <div class="auth-password mb-3">
                        <label for="auth-password">
                            <h5>Пароль</h5>
                        </label>
                        <input id="auth-password" class="form-control" type="password" required>
                    </div>

                    <a class="link mb-3" href="reg">У меня еще нет аккаунта</a>
                    <%--                <a data-toggle="modal" class="link mb-3" href="#sign-up" data-dismiss="modal">У меня еще нет аккаунта</a>--%>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Отмена</button>
                    <button type="submit" class="btn btn-primary float-left">Войти</button>
                </div>
            </form>
        </div>
    </div>
</div>
${open_modal}