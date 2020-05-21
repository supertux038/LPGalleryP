<%@ page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" language="java" %>

<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<%@ include file="/WEB-INF/views/includes/header.incl.jsp" %>
<%@ include file="/WEB-INF/views/includes/navigation.incl.jsp" %>

<main>
    <div class="container pt-5 text-center rounded overflow-hidden">
        <c:if test="${not empty authors}">
            <c:forEach var="author" items="${authors}">
                <div class="container">
                    <div class="author mb-5">
                        <div class="row">
                            <div class="avatar col-2">
                                <img src="${avatar_path}${author.getAvatarPath()}" width="100%"
                                     class="rounded float-left border-light bg-light "
                                     alt="@supertux038_avatar">
                            </div>
                            <div class="author-name text-center col-10 pt-5">
                                <a href="${pageContext.request.contextPath}/user?id=${author.getId()}">
                                    <h1>@${author.getNickname()}</h1>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </c:forEach>
        </c:if>
    </div>
</main>

<%@ include file="/WEB-INF/views/includes/login-modal.incl.jsp" %>

<%@ include file="/WEB-INF/views/includes/footer.incl.jsp" %>

