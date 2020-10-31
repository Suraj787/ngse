import frappe

def comments_and_emails(doc,method=None):
    copy_comments_on_amend(doc)
    copy_emails_on_ammend(doc)

def copy_comments_on_amend(doc,method=None):
    if doc.amended_from:
        comments = frappe.get_list("Comment",filters={"reference_name":doc.amended_from})
        for c in comments:
            comment = frappe.get_doc("Comment",c['name'])
            comment_copy = frappe.copy_doc(comment)
            comment_copy.reference_name = doc.name
            comment_copy.save()
    frappe.db.commit()


def copy_emails_on_ammend(doc,method=None):
    if doc.amended_from:
        # frappe.throw(doc.name)
        emails = frappe.get_list("Communication",filters={"reference_name":doc.amended_from})
        for e in emails:
            email = frappe.get_doc("Communication",e)
            email.reference_name = doc.name
            # el = email.append("timeline_links",{"link_doctype":doc.doctype,"link_name":doc.name})
            email.save()
    frappe.db.commit()