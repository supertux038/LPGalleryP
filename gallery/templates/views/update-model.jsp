<%@ page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" language="java" %>

<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>

<%@ include file="/WEB-INF/views/includes/header.incl.jsp" %>
<%@ include file="/WEB-INF/views/includes/navigation.incl.jsp" %>

<main>
    <div class="container h-auto rounded">
        <form name="add_model" class="pt-5" method="POST" enctype="multipart/form-data">
            <!--            name                     -->
            <input class="form-control form-control-lg col-3 mb-3" type="text" name="name" placeholder="Название модели"
                   value="${model.getName()}" required>
            <!--            description                -->
            <div class="form-group description-input mb-3">
                <label for="description">
                    <h3>Описание</h3>
                </label>
                <textarea class="form-control" rows="5" id="description" name="description">${model.getDescription()}</textarea>
            </div>
            <!--            smaller description        -->
            <div class="form-group description-input mb-3">
                <label for="small-description">
                    <h3>Описание для препросмотра</h3>(максимально 60 символов)
                </label>
                <textarea class="form-control" rows="1" id="small-description" name="sm-description" required>${model.getSmallDescription()}</textarea>
            </div>
            <!--            category                 -->
            <div class="category-input mb-3">
                <label for="category">
                    <h3>Категория</h3>
                </label>
                <select class="form-control col-3" id="category" name="category">
                    <option value="none">Категория</option>
                    <option value="technics">Техника</option>
                    <option value="landscape">Ладндшафт</option>
                    <option value="character">Персонаж</option>
                </select>
            </div>
            <!--            complexity              -->
            <div class="complexity-input mb-3">
                <label for="complexity">
                    <h3>Сложность</h3>
                </label>
                <select class="form-control col-3" id="complexity" name="complexity">
                    <option value="none">Неоцененное</option>
                    <option value="easy">Простое</option>
                    <option value="medium">Средней сложности</option>
                    <option value="hard">Сложное</option>
                </select>
            </div>
            <!--            video                  -->
            <div class="video-input mb-3">
                <label for="video-link">
                    <h3>Видео</h3>
                </label>
                <input type="text" class="form-control col-4" placeholder="https://www.youtube.com/embed/[video_ID]"
                       id="video-link">
            </div>
            <!--            file      -->
            <div class="model-file-input mb-3">
                <label for="model-file-input">
                    <h3>Файл</h3>
                </label><br>
                <div class="custom-file col-4">
                    <input type="file" class="custom-file-input" id="model-file-input" name="file" required>
                    <label class="custom-file-label" for="image-input">Выбирите файл в формате .babylon</label>
                </div>
            </div>
            <!--            image       -->
            <div class="image-input mb-3">
                <label for="image-input">
                    <h3>Картинка для предпросмотра</h3>
                </label><br>
                <div class="custom-file col-4">
                    <input type="file" class="custom-file-input" id="image-input" name="image" required>
                    <label class="custom-file-label" for="image-input">Выберите файл</label>
                </div>
            </div>
            <button class="btn btn-primary mb-5" type="submit">Обновить</button>
        </form>
    </div>
</main>

<%@ include file="/WEB-INF/views/includes/login-modal.incl.jsp" %>

<%@ include file="/WEB-INF/views/includes/footer.incl.jsp" %>


