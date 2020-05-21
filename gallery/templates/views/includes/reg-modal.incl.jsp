<%@page pageEncoding="UTF-8" %>
<%@taglib uri="http://java.sun.com/jstl/core" prefix="c"%>

<div class="modal fade registration-modal" id="sign-up" tabindex="-1" role="dialog"
     aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="sign-up-modal">Регистрация</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <form action="reg" method="post" name="reg">
                <div class="modal-body">
                    <div class="reg-login mb-3">
                        <label for="reg-login">
                            <h5>Никнейм</h5>
                        </label>
                        <input id="reg-login" class="form-control" type="text" name="login" required>
                    </div>
                    <div class="reg-email mb-3">
                        <label for="reg-email">
                            <h5>Электронная почта</h5>
                        </label>
                        <input id="reg-email" class="form-control" type="text" name="email" required>
                    </div>
                    <div class="reg-password mb-3">
                        <label for="reg-password">
                            <h5>Пароль</h5>
                        </label>
                        <input id="reg-password" class="form-control" type="password" name="password" required>
                    </div>
                    <div class="reg-password mb-3">
                        <label for="reg-password-repeat">
                            <h5>Повторите пароль</h5>
                        </label>
                        <input id="reg-password-repeat" class="form-control" type="password" name="password-repeat"
                               required>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Отмена</button>
                    <button type="submit" class="btn btn-primary" id="submit-btn">Зарегистрироваться</button>
                    <script src="../../../static/js/regFormValidation.js"></script>
                </div>
            </form>
        </div>
    </div>
</div>