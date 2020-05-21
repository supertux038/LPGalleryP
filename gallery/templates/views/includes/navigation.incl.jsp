<%@page pageEncoding="UTF-8" %>

<nav class="navbar navbar-expand-xl navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="<c:url value="/main" />">
            <img src="img/logo/applesForLogo.png" width="40" height="40"
                 class="d-inline-block d-sm-none d-md-inline align-top" alt="">
            <span>Low-Poly gallery</span>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <!--                <li class="nav-item active">-->
                <!--                    <a class="nav-link" href="gallery.html">Выставка <span class="sr-only">(current)</span></a>-->
                <!--                </li>-->
<%--                <li class="nav-item">--%>
<%--                    <a class="nav-link" href="#">Туториалы</a>--%>
<%--                </li>--%>
                <li class="nav-item">
                    <a class="nav-link" href="${pageContext.request.contextPath}/authors">Авторы</a>
                </li>
                <li class="nav-item">
                    <%--                    <a class="nav-link" href="#sign-in" data-toggle="modal">Мои модели</a>--%>
                    <a class="nav-link" href="${pageContext.request.contextPath}/${lk_link}"
                    >Мои модели</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2 disabled" type="search" placeholder="Найти автора" aria-label="Search">
                <button class="btn btn-outline-success my-2 mr-sm-2 disabled" type="submit">Поиск</button>
            </form>
        </div>
    </div>
</nav>