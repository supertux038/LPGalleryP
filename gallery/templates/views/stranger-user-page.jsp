<%@ page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" language="java" %>

<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<%@ include file="/WEB-INF/views/includes/header.incl.jsp" %>
<%@ include file="/WEB-INF/views/includes/navigation.incl.jsp" %>

<main>
    <div class="container pb-5 pt-5 rounded overflow-hidden">
        <div class="profile-header">
            <div class="avatar-and-nick w-100 overflow-hidden mb-5 align-content-center row pl-4">
                <div class="avatar col-3">
                    <img src="${avatar_path}${user.getAvatarPath()}" width="100%" class="rounded float-left border-light bg-light "
                         alt="@${user.getId()}_avatar">
                </div>
                <div class="text-user-headers col-6">
                    <div class="nickname">
                        <h2>Никнейм: @${user.getNickname()}</h2>
                    </div>
                    <%--                <div class="role">--%>
                    <%--                    <h4>User</h4>--%>
                    <%--                </div>--%>
                </div>
            </div>
        </div>

        <%--        <c:if test="${empty user.getModels()}">--%>
        <c:if test="${empty models}">
            <div class="no-models text-center">
                <h3>Список моделей пустой</h3>
            </div>
        </c:if>
        <c:if test="${not empty models}">
            <div class="d-flex row" id="models-2">
                <c:forEach var="model" items="${models}">
                    <div class="col-xl-3 col-lg-4">
                        <div class="card m-2">
                            <img class="card-img-top" src="${render_path}${model.getImagePath()}"
                                 alt="${model.getName()}">
                            <div class="card-body">
                                <a class="model-page-link" href="model-page?id=${model.getId()}">
                                    <h5 class="card-title">${model.getName()}</h5>
                                </a>
                                <p class="card-text">${model.getSmallDescription()}</p>
                            </div>
                        </div>
                    </div>
                </c:forEach>
            </div>
        </c:if>
        <%--        </c:if>--%>
        <%--        <div class="d-flex row" id="models-2">--%>
        <%--            <div class="col-xl-3 col-lg-4">--%>
        <%--                <div class="card m-2">--%>
        <%--                    <img class="card-img-top" src="img/renders/86lp.png" alt="AE 86">--%>
        <%--                    <div class="card-body">--%>
        <%--                        <a class="model-page-link" href="#">--%>
        <%--                            <h5 class="card-title">AE 86</h5>--%>
        <%--                        </a>--%>
        <%--                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Excepturi,--%>
        <%--                            suscipit.</p>--%>
        <%--                        <a href="#" class="btn btn-primary">Редактировать</a>--%>
        <%--                    </div>--%>
        <%--                </div>--%>
        <%--            </div>--%>
        <%--            <div class="col-xl-3 col-lg-4">--%>
        <%--                <div class="card m-2">--%>
        <%--                    <img class="card-img-top" src="img/renders/86lp.png" alt="AE 86">--%>
        <%--                    <div class="card-body">--%>
        <%--                        <a class="model-page-link" href="#">--%>
        <%--                            <h5 class="card-title">AE 86</h5>--%>
        <%--                        </a>--%>
        <%--                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Excepturi,--%>
        <%--                            suscipit.</p>--%>
        <%--                        <a href="#" class="btn btn-primary">Редактировать</a>--%>
        <%--                    </div>--%>
        <%--                </div>--%>
        <%--            </div>--%>
        <%--            <div class="col-xl-3 col-lg-4">--%>
        <%--                <div class="card m-2">--%>
        <%--                    <img class="card-img-top" src="img/renders/86lp.png" alt="AE 86">--%>
        <%--                    <div class="card-body">--%>
        <%--                        <a class="model-page-link" href="#">--%>
        <%--                            <h5 class="card-title">AE 86</h5>--%>
        <%--                        </a>--%>
        <%--                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Excepturi,--%>
        <%--                            suscipit.</p>--%>
        <%--                        <a href="#" class="btn btn-primary">Редактировать</a>--%>
        <%--                    </div>--%>
        <%--                </div>--%>
        <%--            </div>--%>
        <%--            <div class="col-xl-3 col-lg-4">--%>
        <%--                <div class="card m-2">--%>
        <%--                    <img class="card-img-top" src="img/renders/86lp.png" alt="AE 86">--%>
        <%--                    <div class="card-body">--%>
        <%--                        <a class="model-page-link" href="#">--%>
        <%--                            <h5 class="card-title">AE 86</h5>--%>
        <%--                        </a>--%>
        <%--                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Excepturi,--%>
        <%--                            suscipit.</p>--%>
        <%--                        <a href="#" class="btn btn-primary">Редактировать</a>--%>
        <%--                    </div>--%>
        <%--                </div>--%>
        <%--            </div>--%>


        <%--        </div>--%>


    </div>

</main>

<%@ include file="/WEB-INF/views/includes/login-modal.incl.jsp" %>

<%@ include file="/WEB-INF/views/includes/footer.incl.jsp" %>

