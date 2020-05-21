<%@ page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@taglib uri="http://java.sun.com/jstl/core" prefix="c" %>

<%@include file="includes/header.incl.jsp" %>
<%@include file="includes/navigation.incl.jsp" %>

<main>
    <div class="container w-25">
        <form name="login" action="login" method="post">
            <div class="modal-body">

                <div class="auth-login mb-3">
                    <label for="auth-login">
                        <h5>Логин</h5>
                    </label>
                    <input id="auth-login" class="form-control ${nick}" name="nickname" type="text" value="${nickname}" required>
                </div>
                <div class="auth-password mb-3">
                    <label for="auth-password">
                        <h5>Пароль</h5>
                    </label>
                    <input id="auth-password" class="form-control ${password}" name="password" type="password" required>
                </div>
                <div class="form-check mb-3">
                    <input class="form-check-input" type="checkbox" value="remember" name="remember-me" id="remember-me-check">
                    <label class="form-check-label" for="remember-me-check">
                        Запомнить меня
                    </label>
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
</main>


<%@include file="includes/footer.incl.jsp" %>
