from . import app
from .models.database import session
from .models.group import Group
from flask import request, render_template, redirect


@app.route("/")
@app.route("/group_management", methods=["POST", "GET"])
def group_management():
    all_groups = session.query(Group).all()
    all_groups = [x.name_of_group for x in all_groups]

    if request.method == "POST":
        name_of_group = request.form.get("name_of_group")
        group = Group(
            name_of_group=name_of_group
        )

        try:
            session.add(group)
            session.commit()
        except Exception as exc:
            return f"При збереженні групи виникла проблема: {exc}"
        finally:
            session.close()
            return redirect("group_management")

    else:
        return render_template("group.html", groups=all_groups)