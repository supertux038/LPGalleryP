<%@ page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@taglib uri="http://java.sun.com/jstl/core" prefix="c" %>

<%@include file="includes/header.incl.jsp" %>
<%@include file="includes/navigation.incl.jsp" %>

<main>
<div class="container w-25">
<form action="reg" method="POST" name="reg">
    <div class="modal-body">
        <div class="reg-login mb-3">
            <label for="reg-login">
                <h5>Никнейм</h5>
            </label>
            <input id="reg-login" class="form-control ${nick}" value="${nick_value}"  type="text" name="login" required>
        </div>
        <div class="reg-email mb-3">
            <label for="reg-email">
                <h5>Электронная почта</h5>
            </label>
            <input id="reg-email" class="form-control ${email}" value="${email_value}" type="text" name="email" required>
        </div>
        <div class="reg-password mb-3">
            <label for="reg-password">
                <h5>Пароль</h5>
            </label>
            <input id="reg-password" class="form-control ${password}" type="password" name="password" required>
        </div>
        <div class="reg-password mb-3">
            <label for="reg-password-repeat">
                <h5>Повторите пароль</h5>
            </label>
            <input id="reg-password-repeat" class="form-control ${password}" type="password" name="password-repeat"
                   required>
            <p>От 8 до 30 символов, обязательно строчные и заглавные буквы, цифры</p>
        </div>
        <select class="form-control form-control-sm mb-3" name="role">
            <option value="user">Пользователь</option>
            <option value="moderator">Модератор</option>
            <option value="admin">Администратор</option>
        </select>
        <div class="form-check mb-3">
            <input class="form-check-input ${agreement}" type="checkbox" value="agree" name="agreement" id="agreement-check" ${checked} required>
            <label class="form-check-label" for="agreement-check">
                Я даю согласие на обработку персональных данных
            </label>
        </div>
    </div>
    <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Отмена</button>
        <button type="submit" class="btn btn-primary" id="submit-btn">Зарегистрироваться</button>
    </div>
</form>
</div>
</main>


<%@include file="includes/footer.incl.jsp" %>
