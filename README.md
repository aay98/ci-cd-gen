# ci-cd-gen

Простой генератор модных DevOps фраз. По итогу генерации фразы она записывается в БД PostgreSQL.
К развернутому приложению также прилагается мониторинг инфраструктуры и мониторинг приложения. Мониторинг инфраструктуры сделан на основе node_exporter с визуализацией в Grafana. Мониторинг приложения сделан на основе flask_monitoring, также с визуализацией в Grafana.

Развертывание приложения происходит посредством docker-compose.

<b>Сервис был написан в качестве решения тестового задания для вакансии Middle DevOps Engineer в zypl.ai</b>

URL для тестирования сервиса: http://137.117.125.137:80/
URL для просмотра метрик: http://137.117.125.137:443/

### Тестовое задание

```text
Ваша задача состоит в следующем:
1. Написать Dockerfile / docker-compose файл.
2. Настроить CI/CD с использованием Github Action / Gitlab CI /
самописные скрипты. Скрипт должен билдить образ и пушить его
на определенный удаленный реестр контейнеров (Docker Hub,
например) и, по возможности, запускать тесты и инструменты
анализа кода
3. Осуществить деплой приложения на Microsoft Azure с
использованием ресурсов WebApp Service или Virtual Machine.
Настроить вебхуки (Azure имеет встроенные инструменты) для
перезапуска сервиса в случае обновления образа в реестре.
4. Прикрутить базу данных к проекту. Движок на свой выбор (MS SQL,
Postgresql, MySQL и т.д.)
5. Прикрутить инструменты телеметрии (observability): мониторинг,
трейсинг, логгинг (на свой выбор: Prometheus + Grafana / Sentry
например, либо более сложные инструменты).
```

